from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName

gato_roboto_base_id: int = 10000

class GatoRobotoItem(Item):
    game = "Gato Roboto"
    
class GatoRobotoItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    
modules_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.module_bigshot: GatoRobotoItemData(gato_roboto_base_id + 212, ItemClassification.progression),
    ItemName.module_coolant: GatoRobotoItemData(gato_roboto_base_id + 211, ItemClassification.progression),
    ItemName.module_decoder: GatoRobotoItemData(gato_roboto_base_id + 209, ItemClassification.progression),
    ItemName.module_hopper: GatoRobotoItemData(gato_roboto_base_id + 214, ItemClassification.progression),
    ItemName.module_missile: GatoRobotoItemData(gato_roboto_base_id + 210, ItemClassification.progression),
    ItemName.module_phase: GatoRobotoItemData(gato_roboto_base_id + 216, ItemClassification.progression),
    ItemName.module_repeater: GatoRobotoItemData(gato_roboto_base_id + 213, ItemClassification.useful),
    ItemName.module_spinjump: GatoRobotoItemData(gato_roboto_base_id + 215, ItemClassification.progression),
}

item_data_table: Dict[str, GatoRobotoItemData] = {
    **modules_item_data_table, 
    ItemName.cartridge: GatoRobotoItemData(gato_roboto_base_id + 217, ItemClassification.progression),
    ItemName.healthkit: GatoRobotoItemData(gato_roboto_base_id + 208, ItemClassification.filler),
    ItemName.progressive_treadmill: GatoRobotoItemData(gato_roboto_base_id + 237, ItemClassification.progression),
    ItemName.progressive_hotboy: GatoRobotoItemData(gato_roboto_base_id + 254, ItemClassification.progression),
    ItemName.progressive_vent: GatoRobotoItemData(gato_roboto_base_id + 2, ItemClassification.progression)
}

item_table = {name: data.code for name, data in item_data_table.items()}