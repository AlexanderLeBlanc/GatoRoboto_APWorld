from typing import Any

gatoroboto_options_presets: dict[str, dict[str, Any]] = {
    "Normal": {
        "rocket_jumps": "vanilla",
        "button_mash": False,
        "precise_input": False,
        "water_mech": False,
        "tiny_mech": False
    },
    "Hard": {
        "rocket_jumps": "chains",
        "button_mash": True,
        "precise_input": True,
        "water_mech": False,
        "tiny_mech": False
    },
    "Glitched": {
        "rocket_jumps": "chains",
        "button_mash": True,
        "precise_input": True,
        "water_mech": True,
        "tiny_mech": True
    }
}