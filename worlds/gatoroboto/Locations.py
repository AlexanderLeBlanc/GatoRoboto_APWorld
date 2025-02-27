from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Names import LocationName
from .Names import RegionName

gatoroboto_base_id: int = 0xCA0000

class GatoRobotoLocation(Location):
    game = "Gato Roboto"
    
class GatoRobotoLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

healthkit_location_data_table: Dict[str, str] = {
    LocationName.healthkit_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 0x00),
    LocationName.healthkit_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 0x01),
    LocationName.healthkit_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 0x02),
    LocationName.healthkit_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 0x03),
    LocationName.healthkit_5: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 0x04),
    LocationName.healthkit_6: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 0x05),
    LocationName.healthkit_7: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 0x06),
    LocationName.healthkit_8: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 0x07),
    LocationName.healthkit_9: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 0x08),
    LocationName.healthkit_10: GatoRobotoLocationData(RegionName.region_6, gatoroboto_base_id + 0x09),
}

cartridge_location_data_table: Dict[str, str] = {
    LocationName.cartridge_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 0x100 + 0x00),
    LocationName.cartridge_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 0x100 + 0x01),
    LocationName.cartridge_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 0x100 + 0x02),
    LocationName.cartridge_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 0x100 + 0x03),
    LocationName.cartridge_5: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 0x100 + 0x04),
    LocationName.cartridge_6: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 0x100 + 0x05),
    LocationName.cartridge_7: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 0x100 + 0x06),
    LocationName.cartridge_8: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 0x100 + 0x07),
    LocationName.cartridge_9: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 0x100 + 0x08),
    LocationName.cartridge_10: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 0x100 + 0x9),
    LocationName.cartridge_11: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 0x100 + 0x10),
    LocationName.cartridge_12: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 0x100 + 0x11),
    LocationName.cartridge_13: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 0x100 + 0x12),
    LocationName.cartridge_14: GatoRobotoLocationData(RegionName.region_6, gatoroboto_base_id + 0x100 + 0x13),
}

module_location_data_table: Dict[str, str] = {
    LocationName.module_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 0x200 + 0x00),
    LocationName.module_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 0x200 + 0x01),
    LocationName.module_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 0x200 + 0x02),
    LocationName.module_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 0x200 + 0x03),
    LocationName.module_5: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 0x200 + 0x04),
    LocationName.module_6: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 0x200 + 0x05),
    LocationName.module_7: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 0x200 + 0x06),
    LocationName.module_8: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 0x200 + 0x07),
}

location_data_table: Dict[str, str] = {
    **healthkit_location_data_table,
    **cartridge_location_data_table,
    **module_location_data_table
}

location_table = {name: data.address for name, data in location_data_table.items()}