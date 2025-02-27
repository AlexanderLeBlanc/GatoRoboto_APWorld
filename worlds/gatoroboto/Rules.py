import math

from BaseClasses import ItemClassification
from worlds.generic.Rules import add_rule, item_name_in_locations, set_rule
from . import Options
from . import GatoRobotoWorld
from .Names import RegionName
from .Names import ItemName
from .Names import LocationName

def set_rules(world: GatoRobotoWorld):    
    #Set Checks for Landing Site
    set_rule(world.get_location(LocationName.healthkit_2),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.cartridge_1),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.cartridge_2),
             lambda state: state.has(ItemName.module_missile, world.player))
    #set event after fan 3
    set_rule(world.get_location(LocationName.module_2),
             lambda state: state.has(ItemName.module_spinjump, world.player))
    
    
    #Set Checks for Nexus
    set_rule(world.get_region(RegionName.region_2).entrances[0],
            lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.healthkit_3), 
             lambda state: state.has(ItemName.module_spinjump, world.player) or (world.options.rocket_jumps and state.has(ItemName.module_coolant, world.player)))
    set_rule(world.get_location(LocationName.healthkit_4), 
             lambda state: state.has(ItemName.module_spinjump, world.player) or (world.options.rocket_jumps))
    #set event after fan 3 or rje
    set_rule(world.get_location(LocationName.cartridge_3), 
             lambda state: world.options.rocket_jumps and state.has(ItemName.module_coolant, world.player))
    set_rule(world.get_location(LocationName.cartridge_4), 
            lambda state: state.has(ItemName.module_spinjump, world.player) or world.options.logic_difficulty == 1)
    #set event fan 3 or van+
    set_rule(world.get_location(LocationName.cartridge_5), 
             lambda state: world.options.logic_difficulty == 1)
    #next two future event rebba 1 & 2
    set_rule(world.get_location(LocationName.module_3), 
             lambda state: state.has(ItemName.cartridge, world.player, 7))
    set_rule(world.get_location(LocationName.module_4), 
             lambda state: state.has(ItemName.cartridge, world.player, 14))
    
    #Set Checks for Aquaducts
    #healthkit 1 treadmill 1
    #healthkit 2 treadmill 3
    set_rule(world.get_location(LocationName.healthkit_7), 
             lambda state: state.has(ItemName.module_spinjump, world.player))
    set_rule(world.get_location(LocationName.cartridge_6), 
            lambda state: state.has(ItemName.module_spinjump, world.player))
    set_rule(world.get_location(LocationName.cartridge_7), 
        lambda state: state.has(ItemName.module_spinjump, world.player))
    #cart 8 treadmill 2
    #spinjump treadmill 3
    
    #Heater Logic
    set_rule(world.get_region(RegionName.region_4).entrances[0],
        lambda state: state.has(ItemName.module_spinjump, world.player) or world.options.rocket_jumps)
    #add events later
    
    #Ventilation logic
    #change to event logic
    set_rule(world.get_region(RegionName.region_5).entrances[0],
        lambda state: (state.has(ItemName.module_spinjump, world.player) or world.options.rocket_jumps))
    
    #Incubator logic
    set_rule(world.get_region(RegionName.region_6).entrances[0],
        lambda state: state.has(ItemName.module_decoder, world.player))
    set_rule(world.get_location(LocationName.healthkit_10), 
            lambda state: state.has(ItemName.module_spinjump, world.player) and state.has(ItemName.module_hopper, world.player) and state.has(ItemName.module_phase, world.player))
    
    
    
    
    
    
    