from copy import deepcopy
from typing import Dict, List

from BaseClasses import ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import GatoRobotoItem, item_table, modules_item_data_table, item_data_table
from .Locations import GatoRobotoLocation, location_table, location_data_table, healthkit_location_data_table, cartridge_location_data_table, module_location_data_table, event_location_data_table
from .Names import ItemName, LocationName
from .Options import GatoRobotoOptions, gatoroboto_option_groups
from multiprocessing import Process
from worlds.LauncherComponents import Component, components

from .Names import RegionName

def run_client():
    print('running gatoroboto client')
    from GatoRobotoClient import main  # lazy import
    p = Process(target=main)
    p.start()

components.append(Component("Gato Roboto Client", "GatoRobotoClient"))

class GatoRobotoWebWorld(WebWorld):
    theme = "ice"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Gato Roboto Archipelago",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Pathkendle", "TheNickRyan"]
    )
    
    tutorials = [setup_en]
    
    option_groups = gatoroboto_option_groups
    
class GatoRobotoWorld(World):
    """Some game description"""
    print("seeing if I can get logs?")
    #Class Data
    game = "Gato Roboto"
    web = GatoRobotoWebWorld()
    options_dataclass = GatoRobotoOptions
    options: GatoRobotoOptions
    location_name_to_id = location_table
    item_name_to_id = item_table
    
    #Instance Data
    def create_item(self, name):
        return GatoRobotoItem(name, item_data_table[name].type, item_data_table[name].code, self.player)
    
    def create_items(self) -> None:
        print("create items?")
        item_pool: List[GatoRobotoItem] = []
        item_count: 32
        item_pool += [self.create_item(name) 
                      for name in modules_item_data_table.keys()]
        
        item_pool += [self.create_item(ItemName.cartridge) for x in range(14)]
        item_pool += [self.create_item(ItemName.healthkit) for x in range(10)]
        item_pool += [self.create_item(ItemName.progressive_vent) for x in range(3)]
        item_pool += [self.create_item(ItemName.progressive_hotboy) for x in range(2)]
        item_pool += [self.create_item(ItemName.progressive_treadmill) for x in range(3)]
        item_pool += [self.create_item(ItemName.hottubes_event)]
        self.multiworld.itempool += item_pool
        
        print("end create items?")
    
    def create_regions(self) -> None:
        from .Regions import region_data_table
        #Create regions
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            
        for loc_name, loc_data in healthkit_location_data_table.items():
            print("Healtkit region: " + str(loc_data.region))
        
        #Create locations
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in healthkit_location_data_table.items()
                if location_data.region == region_name
            })
            region.add_locations({
                location_name: location_data.address for location_name, location_data in cartridge_location_data_table.items()
                if location_data.region == region_name
            })
            region.add_locations({
                location_name: location_data.address for location_name, location_data in module_location_data_table.items()
                if location_data.region == region_name
            })
            region.add_locations({
                location_name: location_data.address for location_name, location_data in event_location_data_table.items()
                if location_data.region == region_name
            })
            
            region.add_exits(region_data_table[region_name].connecting_regions)
            
            print(f"Region: {region_name}, Size: {len(region.locations)}")
            if region_name == RegionName.region_2:
                for location in region.locations:
                    print("Location Info for Region: " + str(location.name))
        
        #Victory logic
        victory_region = self.get_region(RegionName.region_7)
        victory_location = GatoRobotoLocation(self.player, "Gary Defeated", None, victory_region)
        victory_location.place_locked_item(GatoRobotoItem("Victory",  ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        victory_region.locations.append(victory_location)
            
    def get_filler_item_name(self):
        return ItemName.healthkit
    
    def set_rules(self) -> None:
        from .Rules import set_rules
        set_rules(self)
        
    def fill_slot_data(self):
        return {
            "rocket_jumps": self.options.rocket_jumps.value,
            "logic_difficulty": self.options.logic_difficulty.value
        }
        
    print("end of init file")