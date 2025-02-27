from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName

gato_roboto_base_id: int = 0xCA0000

class GatoRobotoItem(Item):
    game = "Gato Roboto"
    
class GatoRobotoItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    
modules_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.module_bigshot: GatoRobotoItemData(gato_roboto_base_id + 0x0, ItemClassification.progression),
    ItemName.module_coolant: GatoRobotoItemData(gato_roboto_base_id + 0x1, ItemClassification.progression),
    ItemName.module_decoder: GatoRobotoItemData(gato_roboto_base_id + 0x2, ItemClassification.progression),
    ItemName.module_hopper: GatoRobotoItemData(gato_roboto_base_id + 0x3, ItemClassification.useful),
    ItemName.module_missile: GatoRobotoItemData(gato_roboto_base_id + 0x4, ItemClassification.progression),
    ItemName.module_phase: GatoRobotoItemData(gato_roboto_base_id + 0x5, ItemClassification.progression),
    ItemName.module_repeater: GatoRobotoItemData(gato_roboto_base_id + 0x6, ItemClassification.useful),
    ItemName.module_spinjump: GatoRobotoItemData(gato_roboto_base_id + 0x7, ItemClassification.progression),
}

item_data_table: Dict[str, GatoRobotoItemData] = {
    **modules_item_data_table, 
    ItemName.cartridge: GatoRobotoItemData(gato_roboto_base_id + 0x8, ItemClassification.filler),
    ItemName.healthkit: GatoRobotoItemData(gato_roboto_base_id + 0x9, ItemClassification.filler)
}

item_table = {name: data.code for name, data in item_data_table.items()}