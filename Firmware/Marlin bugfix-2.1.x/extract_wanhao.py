#!/usr/bin/env python3
"""Extract the build configuration of Wanhao's Marlin 1.1.4 D9 firmwares from their .hex files.

Usage: python3 extract_wanhao.py MK*/Wanhao_factory/**/*.hex > extract.json
Needs avr-objdump (PlatformIO's toolchain-atmelavr, or set AVR_OBJDUMP). See MK*/Wanhao_factory/extract.md.
"""
import glob, hashlib, json, re, struct, subprocess, sys, os
OD = os.environ.get('AVR_OBJDUMP', os.path.expanduser('~/.platformio/packages/toolchain-atmelavr/bin/avr-objdump'))
DT = 16 * 10 / (16000000 / 64 / 256)          # PID_dT for Marlin 1.1.4 on a 16 MHz ATmega2560 = 0.16384

def image(path):
    b = bytearray()
    for l in open(path):
        if l.startswith(':') and l[7:9] == '00':
            b += bytes.fromhex(l[9:9 + 2 * int(l[1:3], 16)])
    return bytes(b)

def disasm(path):
    return subprocess.run([OD, '-D', '-m', 'avr6', '-b', 'ihex', path], capture_output=True, text=True).stdout.splitlines()

def tables(b):
    # reset() keeps DEFAULT_MAX_ACCELERATION (4 x uint32), DEFAULT_MAX_FEEDRATE (4 x float) and
    # DEFAULT_AXIS_STEPS_PER_UNIT (4 x float) side by side, in that order.
    for i in range(32, len(b) - 16):
        s = struct.unpack('<4f', b[i:i + 16])
        if 70 < s[0] < 90 and 70 < s[1] < 90 and 300 < s[2] < 1700 and 80 < s[3] < 200:
            return dict(steps=[round(x, 3) for x in s],
                        max_feedrate=[round(x, 3) for x in struct.unpack('<4f', b[i - 16:i])],
                        max_accel=list(struct.unpack('<4I', b[i - 32:i - 16])))
    return {}

def pid(b):
    # Temperature keeps Kd/dT, Ki*dT, Kp as three consecutive floats in the .data image.
    for i in range(len(b) - 12):
        kd, ki, kp = struct.unpack('<3f', b[i:i + 12])
        if 5 < kp < 80 and 0.01 < ki < 1.5 and 50 < kd < 5000:
            Ki, Kd = ki / DT, kd * DT
            if 0.1 < Ki < 10 and 20 < Kd < 500:
                return [round(kp, 2), round(Ki, 2), round(Kd, 2)]
    return None

def volume(b):
    # soft_endstop_max = { X_MAX_POS, Y_MAX_POS, Z_MAX_POS } as three consecutive floats.
    sizes = (300.0, 400.0, 500.0)
    for i in range(len(b) - 12):
        x, y, z = struct.unpack('<3f', b[i:i + 12])
        if x in sizes and y in sizes and z in (400.0, 500.0):
            return [x, y, z]
    return None

DIRMASK = {'01': ('X', 1), 'fe': ('X', 0), '08': ('Y', 1), 'f7': ('Y', 0), '80': ('Z', 1), '7f': ('Z', 0)}
def directions(L):
    # Stepper::set_directions(): X, Y, Z DIR pins are PK0, PK3, PK7 (PORTK, data address 0x0108).
    # Each axis writes INVERT first (negative move) then !INVERT; set-then-clear means INVERT true.
    ops = []
    for i, l in enumerate(L):
        m = re.search(r'\b(ori|andi)\s+r\d+,\s*0x([0-9a-fA-F]{2})', l)
        if m and m.group(2).lower() in DIRMASK and any('0x0108' in L[j] for j in range(max(0, i - 3), min(i + 4, len(L)))):
            ops.append((i,) + DIRMASK[m.group(2).lower()])
    for k in range(len(ops) - 5):
        w = ops[k:k + 6]
        if [x[1] for x in w] == list('XXYYZZ') and w[5][0] - w[0][0] < 120:
            r = {ax: [x for x in w if x[1] == ax] for ax in 'XYZ'}
            res = {ax: (a[2], b_[2]) == (1, 0) for ax, (a, b_) in r.items()}
            # E0 DIR is PF5: sbi/cbi on I/O 0x11 bit 5, right after Z.
            e = [('sbi' if 'sbi' in s else 'cbi') for s in L[w[5][0]:w[5][0] + 80] if re.search(r'\b(sbi|cbi)\s+0x11,\s*5\b', s)]
            res['E0'] = e[:2] == ['sbi', 'cbi'] if e[:2] in (['sbi', 'cbi'], ['cbi', 'sbi']) else None
            return res
    return None

def pin_reads(L, addr, bit):
    # count bit tests of an input register read through lds (PINH = 0x0100), with the skip opcode used
    out = []
    for i, l in enumerate(L):
        m = re.search(rf'\blds\s+r(\d+),\s*{addr}\b', l)
        if m:
            for j in range(i + 1, min(i + 5, len(L))):
                t = re.search(rf'\b(sbrc|sbrs)\s+r{m.group(1)},\s*{bit}\b', L[j])
                if t: out.append(t.group(1)); break
    return out

def io_reads(L, port, bit):
    return [m.group(1) for l in L for m in [re.search(rf'\b(sbic|sbis)\s+{port},\s*{bit}\b', l)] if m]

def analyse(path):
    b = image(path); L = disasm(path); s = b.decode('latin-1')
    comp = re.search(r'Compiled: (\w{3} +\d+ \d{4})', s)
    return dict(
        file=path, sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(), code_bytes=len(b),
        compiled=comp.group(1) if comp else None,
        marlin=(re.search(r'FIRMWARE_NAME:Marlin (\S+)', s) or re.search(r'Marlin (\d\.\d\.\d)', s)).group(1),
        machine_type=(re.search(r'MACHINE_TYPE:(\w+)', s) or [None, None])[1],
        bltouch=bool(re.search(r'(?i)bltouch', s)),
        **tables(b), pid_hotend=pid(b), volume=volume(b), invert=directions(L),
        filament_reads=pin_reads(L, '0x0100', 5),        # FIL_RUNOUT_PIN 8 = PH5
        power_loss_reads=pin_reads(L, '0x0106', 1),      # POWER_LOSS_PIN 63 = PK1 (PINK)
        endstop_reads=dict(X=io_reads(L, '0x0f', 0),     # X_MIN_PIN 54 = PF0 (PINF, I/O 0x0F)
                           Y=io_reads(L, '0x00', 2),     # Y_MIN_PIN 24 = PA2 (PINA, I/O 0x00)
                           Z=pin_reads(L, '0x0100', 3)), # Z_MIN_PIN 6  = PH3 (PINH)
    )

if __name__ == '__main__':
    res = [analyse(p) for p in sys.argv[1:]]
    json.dump(res, sys.stdout, indent=1)
