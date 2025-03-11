from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Names import LocationName
from .Names import RegionName

gatoroboto_base_id: int = 10000

class GatoRobotoLocation(Location):
    game = "Gato Roboto"
    
class GatoRobotoLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

healthkit_location_data_table: Dict[str, str] = {
    LocationName.healthkit_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 0),
    LocationName.healthkit_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 1),
    LocationName.healthkit_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 2),
    LocationName.healthkit_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 3),
    LocationName.healthkit_5: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 4),
    LocationName.healthkit_6: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 5),
    LocationName.healthkit_7: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 6),
    LocationName.healthkit_8: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 7),
    LocationName.healthkit_9: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 8),
    LocationName.healthkit_10: GatoRobotoLocationData(RegionName.region_6, gatoroboto_base_id + 9),
}

cartridge_location_data_table: Dict[str, str] = {
    LocationName.cartridge_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 100 + 0),
    LocationName.cartridge_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 100 + 1),
    LocationName.cartridge_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 100 + 2),
    LocationName.cartridge_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 100 + 3),
    LocationName.cartridge_5: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 100 + 4),
    LocationName.cartridge_6: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 100 + 5),
    LocationName.cartridge_7: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 100 + 6),
    LocationName.cartridge_8: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 100 + 7),
    LocationName.cartridge_9: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 100 + 8),
    LocationName.cartridge_10: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 100 + 9),
    LocationName.cartridge_11: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 100 + 10),
    LocationName.cartridge_12: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 100 + 11),
    LocationName.cartridge_13: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 100 + 12),
    LocationName.cartridge_14: GatoRobotoLocationData(RegionName.region_6, gatoroboto_base_id + 100 + 13),
}

module_location_data_table: Dict[str, str] = {
    LocationName.module_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 200 + 0),
    LocationName.module_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 200 + 1),
    LocationName.module_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 200 + 2),
    LocationName.module_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 200 + 3),
    LocationName.module_5: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 200 + 4),
    LocationName.module_6: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 200 + 5),
    LocationName.module_7: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 200 + 6),
    LocationName.module_8: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 200 + 7),
}

event_location_data_table: Dict[str, str] = {
    LocationName.treadmill_1: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 300 + 0),
    LocationName.treadmill_2: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 300 + 1),
    LocationName.treadmill_3: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 300 + 2),
    LocationName.hotboy_1: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 300 + 3),
    LocationName.hotboy_2: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 300 + 4),
    LocationName.hottubes: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 300 + 5),
    LocationName.vent_button_1: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 300 + 6),
    LocationName.vent_button_2: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 300 + 7),
    LocationName.vent_button_3: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 300 + 8)
}

location_data_table: Dict[str, str] = {
    **healthkit_location_data_table,
    **cartridge_location_data_table,
    **module_location_data_table,
    **event_location_data_table
}

location_table = {name: data.address for name, data in location_data_table.items()}