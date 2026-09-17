#!/usr/bin/env python3
"""Generate UltiMaker Cura and OrcaSlicer profiles for the 12 Wanhao Duplicator 9 firmwares.

Run from anywhere: python3 Slicer/build_profiles.py [dist_dir]
Writes Slicer/Cura/<printer>/ and Slicer/OrcaSlicer/<printer>/, and, when dist_dir is given, the files attached to
a release: D9_<model>_<size>_Cura.zip and D9_<model>_<size>.orca_printer.

The machine values come from the Duplicator 9 configurations these firmwares are built from
(config/examples/Wanhao/Duplicator 9 in MarlinFirmware/Configurations): bed size, height, maximum feedrates,
accelerations, jerk and the highest bed temperature each model accepts. Every D9 has a direct-drive MK10 extruder,
a 0.4 mm nozzle and 1.75 mm filament. The firmware limits the extruder to 25 mm/s, so retractions stay at that speed.
"""
import json
import shutil
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERSION = "2.0.9"

SIZES = {"300": (300, 300, 400), "400": (400, 400, 400), "500": (500, 500, 500)}
# Per model: max acceleration X/Y/E, printing, travel and retract acceleration, BED_MAXTEMP per size.
MODELS = {
    "MK1": dict(accel_max=500, accel_print=500, accel_travel=500, accel_retract=800,
                bed_maxtemp={"300": 115, "400": 115, "500": 115}),
    "MK1u2": dict(accel_max=3000, accel_print=800, accel_travel=1000, accel_retract=800,
                  bed_maxtemp={"300": 125, "400": 125, "500": 125}),
    "MK2": dict(accel_max=3000, accel_print=800, accel_travel=1000, accel_retract=800,
                bed_maxtemp={"300": 125, "400": 125, "500": 125}),
    "MK3": dict(accel_max=3000, accel_print=800, accel_travel=1000, accel_retract=800,
                bed_maxtemp={"300": 105, "400": 105, "500": 90}),
}
MAX_FEEDRATE = dict(x=300, y=300, z=5, e=25)
JERK = dict(xy=10, z=0.4, e=1)
HOTEND_MAXTEMP = 305
HOTEND_OVERSHOOT, BED_OVERSHOOT = 15, 10       # Marlin refuses targets above MAXTEMP minus these

RETRACT_LENGTH, RETRACT_SPEED = 1.5, 25
PRIME_LINE_WIDTH, PRIME_LINE_HEIGHT = 0.6, 0.3
SPEED = dict(print=60, outer_wall=40, inner_wall=60, infill=70, top=40, first_layer=20, travel=150, support=50,
             bridge=30)

# Filaments for OrcaSlicer (Cura has its own material library). Standalone presets, so they import into any OrcaSlicer
# version; the material values are those of OrcaSlicer's Generic PLA / PETG.
FILAMENTS = {
    "PLA": dict(nozzle=205, nozzle_first=210, bed=60, bed_first=65, fan_min=100, fan_max=100, fan_off_layers=1,
                density=1.24, cost=20, flow=0.98, max_volumetric=12, range=(190, 240), vitrification=45,
                slow_layer_time=4, cooling_layer_time=100, overhang_threshold="50%"),
    "PETG": dict(nozzle=235, nozzle_first=240, bed=75, bed_first=80, fan_min=30, fan_max=50, fan_off_layers=3,
                 density=1.27, cost=30, flow=1, max_volumetric=10, range=(220, 260), vitrification=70,
                 slow_layer_time=8, cooling_layer_time=20, overhang_threshold="95%"),
    # Wanhao gives the D9's hotend for materials melting at up to 250 °C, so ABS stays at 245.
    "ABS": dict(nozzle=245, nozzle_first=245, bed=100, bed_first=105, fan_min=10, fan_max=30, fan_off_layers=3,
                density=1.04, cost=20, flow=0.926, max_volumetric=12, range=(230, 250), vitrification=110,
                slow_layer_time=3, cooling_layer_time=30, overhang_threshold="25%"),
}
PROCESSES = {"Fine": 0.12, "Standard": 0.20, "Draft": 0.28}


def start_gcode(bed, nozzle, relative_e, depth, bltouch):
    """Heat, home, then draw a priming line 15 mm from the left edge, clear of the bed clips."""
    y0, y1 = 20, 20 + min(120, round(depth * 0.4))
    e = round((y1 - y0) * PRIME_LINE_WIDTH * PRIME_LINE_HEIGHT / (3.14159 * (1.75 / 2) ** 2), 1)
    return "\n".join([
        "; Wanhao Duplicator 9 start G-code",
        "G21 ; millimetres",
        "G90 ; absolute coordinates",
        "M83 ; relative extrusion" if relative_e else "M82 ; absolute extrusion",
        f"M140 S{bed} ; heat the bed",
        "M104 S150 ; warm the nozzle without letting it ooze",
        "G91 ; a print stopped by hand can leave the nozzle down on the bed",
        "G1 Z10 F300 ; so raise it before homing: a BLTouch needs 10 mm to deploy",
        "G90",
        *(["M280 P0 S160 ; BLTouch: clear an alarm and stow the pin"] if bltouch else []),
        "G28 ; home all axes (this turns bed levelling off)",
        "M420 S1 ; turn the bed mesh saved from the screen back on",
        "G1 Z10 F300",
        f"M190 S{bed} ; wait for the bed",
        f"M109 S{nozzle} ; wait for the nozzle",
        "G92 E0",
        f"G1 X15 Y{y0} Z{PRIME_LINE_HEIGHT} F3000 ; start of the priming line",
        f"G1 Y{y1} E{e} F1200 ; draw a line of filament",
        "G1 X15.5 F3000",
        f"G1 Y{y0} E{e if relative_e else 2 * e} F1200 ; and back, next to it",
        "G92 E0",
        "G1 X22 F6000 ; wipe sideways to snap the string",
        "G1 Z2 F300 ; lift, so the line does not stick to the nozzle",
    ])


def end_gcode(depth):
    return "\n".join([
        "; Wanhao Duplicator 9 end G-code",
        "M104 S0 ; nozzle heater off",
        "M140 S0 ; bed heater off",
        "M107 ; fan off",
        "G91 ; relative moves",
        "G1 E-2 F1500 ; release the pressure in the nozzle",
        "G1 Z10 F300 ; lift the nozzle",
        "G90 ; absolute moves",
        f"G1 X5 Y{depth - 10} F3000 ; bring the bed to the front",
        "M84 X Y E ; motors off, Z keeps its position",
    ])


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- UltiMaker Cura

def cura(model, size, out):
    m, (w, d, h) = MODELS[model], SIZES[size]
    ident = f"wanhao_d9_{model.lower()}_{size}"
    name = f"Wanhao D9 {model} {size}"
    bed_max_target = m["bed_maxtemp"][size] - BED_OVERSHOOT
    dv = lambda v: {"default_value": v}  # noqa: E731
    definition = {
        "version": 2,
        "name": name,
        "inherits": "fdmprinter",
        "metadata": {
            "visible": True,
            "author": "Le-Syl21",
            "manufacturer": "Wanhao",
            "file_formats": "text/x-gcode",
            "has_materials": True,
            "preferred_quality_type": "draft",
            "machine_extruder_trains": {"0": f"{ident}_extruder_0"},
        },
        "overrides": {
            "machine_name": dv(name),
            "machine_width": dv(w),
            "machine_depth": dv(d),
            "machine_height": dv(h),
            "machine_heated_bed": dv(True),
            "machine_center_is_zero": dv(False),
            "machine_gcode_flavor": dv("RepRap (Marlin/Sprinter)"),
            "machine_start_gcode": dv(start_gcode("{material_bed_temperature_layer_0}",
                                                  "{material_print_temperature_layer_0}", False, d, model != "MK1")),
            "machine_end_gcode": dv(end_gcode(d)),
            "machine_max_feedrate_x": dv(MAX_FEEDRATE["x"]),
            "machine_max_feedrate_y": dv(MAX_FEEDRATE["y"]),
            "machine_max_feedrate_z": dv(MAX_FEEDRATE["z"]),
            "machine_max_feedrate_e": dv(MAX_FEEDRATE["e"]),
            "machine_max_acceleration_x": dv(m["accel_max"]),
            "machine_max_acceleration_y": dv(m["accel_max"]),
            "machine_max_acceleration_z": dv(100),
            "machine_max_acceleration_e": dv(m["accel_max"]),
            "machine_acceleration": dv(m["accel_print"]),
            "machine_max_jerk_xy": dv(JERK["xy"]),
            "machine_max_jerk_z": dv(JERK["z"]),
            "machine_max_jerk_e": dv(JERK["e"]),
            "material_print_temperature": {"maximum_value": str(HOTEND_MAXTEMP - HOTEND_OVERSHOOT)},
            "material_print_temperature_layer_0": {"maximum_value": str(HOTEND_MAXTEMP - HOTEND_OVERSHOOT)},
            "material_bed_temperature": {"maximum_value": str(bed_max_target),
                                         "maximum_value_warning": str(bed_max_target)},
            "material_bed_temperature_layer_0": {"maximum_value": str(bed_max_target),
                                                 "maximum_value_warning": str(bed_max_target)},
            "retraction_amount": dv(RETRACT_LENGTH),
            "retraction_speed": dv(RETRACT_SPEED),
            "retraction_hop_enabled": dv(False),
            "retraction_combing": {"value": "'noskin'"},
            "speed_print": dv(SPEED["print"]),
            "speed_wall_0": {"value": str(SPEED["outer_wall"])},
            "speed_wall_x": {"value": str(SPEED["inner_wall"])},
            "speed_infill": {"value": str(SPEED["infill"])},
            "speed_topbottom": {"value": str(SPEED["top"])},
            "speed_support": {"value": str(SPEED["support"])},
            "speed_layer_0": {"value": str(SPEED["first_layer"])},
            "speed_travel": {"value": str(SPEED["travel"])},
            "speed_z_hop": {"value": str(MAX_FEEDRATE["z"])},
            "wall_thickness": {"value": "1.2"},
            "top_thickness": {"value": "0.8"},
            "bottom_thickness": {"value": "0.6"},
            "infill_sparse_density": dv(15),
            "infill_pattern": {"value": "'gyroid'"},
            "acceleration_enabled": dv(False),
            "jerk_enabled": dv(False),
            "layer_height_0": dv(0.2),
            "adhesion_type": dv("skirt"),
            "skirt_line_count": dv(2),
            "support_enable": dv(False),
            "cool_fan_full_layer": {"value": "2"},
        },
    }
    extruder = {
        "version": 2,
        "name": "Extruder 1",
        "inherits": "fdmextruder",
        "metadata": {"machine": ident, "position": "0"},
        "overrides": {
            "extruder_nr": {"default_value": 0},
            "machine_nozzle_size": {"default_value": 0.4},
            "material_diameter": {"default_value": 1.75},
        },
    }
    base = out / "Cura" / f"D9_{model}_{size}"
    write_json(base / "definitions" / f"{ident}.def.json", definition)
    write_json(base / "extruders" / f"{ident}_extruder_0.def.json", extruder)
    return base


# ---------------------------------------------------------------- OrcaSlicer

def orca(model, size, out):
    m, (w, d, h) = MODELS[model], SIZES[size]
    printer = f"Wanhao D9 {model} {size} 0.4 nozzle"
    two = lambda v: [str(v), str(v)]  # noqa: E731  normal and silent mode
    presets = []
    presets.append(("printer", printer, {
        "type": "machine", "name": printer, "from": "User", "inherits": "", "version": VERSION,
        "printer_settings_id": printer, "printer_technology": "FFF", "printer_variant": "0.4",
        "printer_notes": "Wanhao Duplicator 9 " + model + " " + size + ", firmware https://github.com/Le-Syl21/WANHAO-Duplicator-9",
        "gcode_flavor": "marlin2", "use_relative_e_distances": "1", "emit_machine_limits_to_gcode": "0",
        "printable_area": ["0x0", f"{w}x0", f"{w}x{d}", f"0x{d}"], "printable_height": str(h),
        "nozzle_diameter": ["0.4"], "max_layer_height": ["0.32"], "min_layer_height": ["0.08"],
        "machine_max_speed_x": two(MAX_FEEDRATE["x"]), "machine_max_speed_y": two(MAX_FEEDRATE["y"]),
        "machine_max_speed_z": two(MAX_FEEDRATE["z"]), "machine_max_speed_e": two(MAX_FEEDRATE["e"]),
        "machine_max_acceleration_x": two(m["accel_max"]), "machine_max_acceleration_y": two(m["accel_max"]),
        "machine_max_acceleration_z": two(100), "machine_max_acceleration_e": two(m["accel_max"]),
        "machine_max_acceleration_extruding": two(m["accel_print"]),
        "machine_max_acceleration_travel": two(m["accel_travel"]),
        "machine_max_acceleration_retracting": two(m["accel_retract"]),
        "machine_max_jerk_x": two(JERK["xy"]), "machine_max_jerk_y": two(JERK["xy"]),
        "machine_max_jerk_z": two(JERK["z"]), "machine_max_jerk_e": two(JERK["e"]),
        "retraction_length": [str(RETRACT_LENGTH)], "retraction_speed": [str(RETRACT_SPEED)],
        "deretraction_speed": [str(RETRACT_SPEED)], "retraction_minimum_travel": ["1"], "z_hop": ["0"],
        "retract_when_changing_layer": ["1"], "wipe": ["0"],
        "machine_start_gcode": start_gcode("[bed_temperature_initial_layer_single]",
                                           "[nozzle_temperature_initial_layer]", True, d, model != "MK1"),
        "machine_end_gcode": end_gcode(d),
        "layer_change_gcode": "G92 E0 ; relative extrusion: reset E on each layer",
        "machine_pause_gcode": "M600", "change_filament_gcode": "M600",
        "default_print_profile": f"0.20mm Standard @{printer}",
        "default_filament_profile": [f"D9 PLA @{printer}"],
    }))
    for label, layer in PROCESSES.items():
        name = f"{layer:.2f}mm {label} @{printer}"
        presets.append(("process", name, {
            "type": "process", "name": name, "from": "User", "inherits": "", "version": VERSION,
            "print_settings_id": name, "compatible_printers": [printer],
            "layer_height": f"{layer:.2f}", "initial_layer_print_height": "0.2",
            "wall_loops": "3", "top_shell_layers": str(max(4, round(0.8 / layer))),
            "bottom_shell_layers": str(max(3, round(0.6 / layer))),
            "sparse_infill_density": "15%", "sparse_infill_pattern": "gyroid",
            "outer_wall_speed": str(SPEED["outer_wall"]), "inner_wall_speed": str(SPEED["inner_wall"]),
            "sparse_infill_speed": str(SPEED["infill"]), "internal_solid_infill_speed": str(SPEED["infill"]),
            "top_surface_speed": str(SPEED["top"]), "gap_infill_speed": str(SPEED["top"]),
            "bridge_speed": str(SPEED["bridge"]), "support_speed": str(SPEED["support"]),
            "initial_layer_speed": str(SPEED["first_layer"]), "initial_layer_infill_speed": str(SPEED["first_layer"]),
            "travel_speed": str(SPEED["travel"]),
            "default_acceleration": str(m["accel_print"]), "outer_wall_acceleration": str(m["accel_print"]),
            "inner_wall_acceleration": str(m["accel_print"]), "top_surface_acceleration": str(m["accel_print"]),
            "sparse_infill_acceleration": str(m["accel_print"]), "initial_layer_acceleration": str(m["accel_print"]), "bridge_acceleration": str(m["accel_print"]),
            "travel_acceleration": str(m["accel_travel"]),
            "default_jerk": "0", "skirt_loops": "2", "skirt_distance": "5", "brim_type": "no_brim",
            "enable_support": "0", "enable_arc_fitting": "0",
        }))
    bed_max = m["bed_maxtemp"][size] - BED_OVERSHOOT
    for label, f in FILAMENTS.items():
        name = f"D9 {label} @{printer}"
        plate = lambda v: [str(v)]  # noqa: E731
        # The bed cannot be asked for more than the firmware allows (MK3 500: 80 °C, so no real ABS bed).
        bed, bed_first = min(f["bed"], bed_max), min(f["bed_first"], bed_max)
        presets.append(("filament", name, {
            "type": "filament", "name": name, "from": "User", "inherits": "", "version": VERSION,
            "filament_settings_id": [name], "compatible_printers": [printer], "filament_diameter": ["1.75"],
            "filament_type": [label], "filament_vendor": ["Generic"], "filament_density": plate(f["density"]),
            "filament_cost": plate(f["cost"]), "filament_flow_ratio": plate(f["flow"]),
            "filament_max_volumetric_speed": plate(f["max_volumetric"]),
            "nozzle_temperature_range_low": plate(f["range"][0]), "nozzle_temperature_range_high": plate(f["range"][1]),
            "temperature_vitrification": plate(f["vitrification"]), "slow_down_layer_time": plate(f["slow_layer_time"]),
            "slow_down_min_speed": ["10"], "fan_cooling_layer_time": plate(f["cooling_layer_time"]),
            "overhang_fan_speed": ["100"], "overhang_fan_threshold": [f["overhang_threshold"]],
            "reduce_fan_stop_start_freq": ["1"],
            "nozzle_temperature": plate(f["nozzle"]), "nozzle_temperature_initial_layer": plate(f["nozzle_first"]),
            **{f"{p}_plate_temp": plate(bed) for p in ("cool", "eng", "hot", "textured", "supertack")},
            **{f"{p}_plate_temp_initial_layer": plate(bed_first) for p in ("cool", "eng", "hot", "textured", "supertack")},
            "fan_min_speed": plate(f["fan_min"]), "fan_max_speed": plate(f["fan_max"]),
            "close_fan_the_first_x_layers": plate(f["fan_off_layers"]),
        }))
    base = out / "OrcaSlicer" / f"D9_{model}_{size}"
    if base.exists():
        shutil.rmtree(base)
    files = {"printer": [], "process": [], "filament": []}
    for kind, name, data in presets:
        rel = f"{kind}/{name}.json"
        write_json(base / rel, data)
        files[kind].append(rel)
    bundle = {"version": VERSION, "bundle_id": f"Le-Syl21_D9_{model}_{size}", "bundle_type": "printer config bundle",
              "printer_preset_name": printer, "printer_config": files["printer"],
              "filament_config": files["filament"], "process_config": files["process"]}
    write_json(base / "bundle_structure.json", bundle)
    return base


def main():
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if dist:
        dist.mkdir(parents=True, exist_ok=True)
    for model in MODELS:
        for size in SIZES:
            c, o = cura(model, size, HERE), orca(model, size, HERE)
            if not dist:
                continue
            with zipfile.ZipFile(dist / f"D9_{model}_{size}_Cura.zip", "w", zipfile.ZIP_DEFLATED) as z:
                for p in sorted(c.rglob("*.json")):
                    z.write(p, p.relative_to(c))
            with zipfile.ZipFile(dist / f"D9_{model}_{size}.orca_printer", "w", zipfile.ZIP_DEFLATED) as z:
                for p in sorted(o.rglob("*.json")):
                    z.write(p, p.relative_to(o))
    print("profiles written" + (f", release files in {dist}" if dist else ""))


if __name__ == "__main__":
    main()
