import math

from BaseClasses import ItemClassification
from worlds.generic.Rules import add_rule, item_name_in_locations, set_rule
from . import Options
from . import GatoRobotoWorld
from .Names import RegionName
from .Names import ItemName
from .Names import LocationName

from .Locations import GatoRobotoLocation

def set_rules(world: GatoRobotoWorld):    
    #Set Checks for Landing Site
    set_rule(world.get_location(LocationName.healthkit_2),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.cartridge_1),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.cartridge_2),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.module_2),
             lambda state: state.has(ItemName.module_spinjump, world.player) and state.has(ItemName.progressive_vent, world.player, 3))
    
    
    #Set Checks for Nexus
    set_rule(world.get_region(RegionName.region_2).entrances[0],
            lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.healthkit_3), 
             lambda state: state.has(ItemName.module_spinjump, world.player) or (world.options.rocket_jumps and state.has(ItemName.module_coolant, world.player)))
    set_rule(world.get_location(LocationName.healthkit_4), 
             lambda state: state.has(ItemName.module_spinjump, world.player) or (world.options.rocket_jumps))
    set_rule(world.get_location(LocationName.cartridge_3), 
             lambda state: state.has(ItemName.progressive_aqueduct, world.player, 3) or (world.options.rocket_jumps and state.has(ItemName.module_coolant, world.player)))
    set_rule(world.get_location(LocationName.cartridge_4), 
            lambda state: state.has(ItemName.module_spinjump, world.player) or world.options.logic_difficulty == 1)
    set_rule(world.get_location(LocationName.cartridge_5), 
             lambda state: state.has(ItemName.progressive_vent, world.player, 3) or world.options.logic_difficulty == 1)
    set_rule(world.get_location(LocationName.module_3), 
             lambda state: state.has(ItemName.cartridge, world.player, 7))
    set_rule(world.get_location(LocationName.module_4), 
             lambda state: state.has(ItemName.cartridge, world.player, 14))
    
    #Set Checks for Aquaducts
    set_rule(world.get_location(LocationName.healthkit_5), 
            lambda state: state.has(ItemName.progressive_aqueduct, world.player, 1))
    set_rule(world.get_location(LocationName.healthkit_6), 
             lambda state: state.has(ItemName.progressive_aqueduct, world.player, 3))
    set_rule(world.get_location(LocationName.cartridge_6), 
            lambda state: state.has(ItemName.module_spinjump, world.player) and state.has(ItemName.progressive_aqueduct, world.player, 3))
    set_rule(world.get_location(LocationName.cartridge_7), 
             lambda state: state.has(ItemName.module_spinjump, world.player) and state.has(ItemName.progressive_aqueduct, world.player, 3))
    set_rule(world.get_location(LocationName.cartridge_8), 
             lambda state: state.has(ItemName.progressive_aqueduct, world.player, 2))
    set_rule(world.get_location(LocationName.module_5), 
             lambda state: state.has(ItemName.progressive_aqueduct, world.player, 3))
    set_rule(world.get_location(LocationName.aqueduct_2), 
             lambda state: state.has(ItemName.progressive_aqueduct, world.player, 1))
    set_rule(world.get_location(LocationName.aqueduct_3), 
             lambda state: state.has(ItemName.progressive_aqueduct, world.player, 2))
    
    #Heater Logic
    set_rule(world.get_region(RegionName.region_4).entrances[0],
             lambda state: state.has(ItemName.module_spinjump, world.player) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.healthkit_7), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 3) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.healthkit_8), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 3) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.cartridge_9), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 3) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.cartridge_10), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 3) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.cartridge_11), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 3) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.module_6), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 3) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.module_7), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 2) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.heater_3), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 2))
    set_rule(world.get_location(LocationName.heater_2), 
             lambda state: state.has(ItemName.progressive_heater, world.player, 1))
    
    #Ventilation logic
    set_rule(world.get_region(RegionName.region_5).entrances[0],
        lambda state: state.has(ItemName.progressive_aqueduct, world.player, 3) and state.has(ItemName.progressive_heater, world.player, 3))
    set_rule(world.get_location(LocationName.healthkit_9), 
             lambda state: state.has(ItemName.progressive_vent, world.player, 1))
    set_rule(world.get_location(LocationName.cartridge_12), 
             lambda state: state.has(ItemName.progressive_vent, world.player, 3))
    set_rule(world.get_location(LocationName.cartridge_13), 
             lambda state: state.has(ItemName.progressive_vent, world.player, 3))
    set_rule(world.get_location(LocationName.module_8), 
             lambda state: state.has(ItemName.progressive_vent, world.player, 1))
    set_rule(world.get_location(LocationName.vent_2), 
             lambda state: state.has(ItemName.progressive_vent, world.player, 1))
    set_rule(world.get_location(LocationName.vent_3), 
             lambda state: state.has(ItemName.progressive_vent, world.player, 2))
    
    #Incubator logic
    set_rule(world.get_region(RegionName.region_6).entrances[0],
        lambda state: state.has(ItemName.module_decoder, world.player) and state.has(ItemName.progressive_vent, world.player, 3) and state.has(ItemName.progressive_heater, world.player, 3))
    set_rule(world.get_location(LocationName.healthkit_10), 
            lambda state: state.has(ItemName.module_spinjump, world.player) and state.has(ItemName.module_hopper, world.player) and state.has(ItemName.module_phase, world.player))
    
    
    
    
    
    
    
    