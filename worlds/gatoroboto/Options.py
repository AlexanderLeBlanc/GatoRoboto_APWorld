from dataclasses import dataclass

## Add deathlink later!!!
from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions

class ButtonMash(Toggle):
    """
        Option to enable areas and checks that can be accessed early through button mashing
    """
    display_name = "Button Mash Areas"
    
class PreciseInput(Toggle):
    """
        Option to enable areas and checks that can be accessed early through precise input
    """
    display_name = "Precise Input Areas"
        
class WaterMech(Toggle):
    """
        Option to enable areas and checks that can be accessed early through the water mech glitch
    """
    display_name = "Water Mech Areas"
            
class TinyMech(Toggle):
    """
        Option to enable areas and checks that can be accessed early through the tiny mech glitch
    """
    display_name = "Tiny Mech Areas"

class RocketJumps(Choice):
    """
        Vanilla: the game as it was intended
        Single Jumps: checks accessed through a single rocket jump
        Chained Jumps: checks accessed through a one or more rocket jump
    """
    display_name = "Rocket Jump Options"
    option_vanilla = 0
    option_single = 1
    option_chains = 2
    default = 0
    
gatoroboto_option_groups = [
    OptionGroup("Logic Options", [
        RocketJumps,
        ButtonMash,
        PreciseInput,
        WaterMech,
        TinyMech
    ])
]

@dataclass
class GatoRobotoOptions(PerGameCommonOptions):
    rocket_jumps: RocketJumps
    button_mash: ButtonMash
    precise_input: PreciseInput
    water_mech: WaterMech
    tiny_mech: TinyMech