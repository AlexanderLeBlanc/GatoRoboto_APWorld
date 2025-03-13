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

cartidges_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.cartridge_1: GatoRobotoItemData(gato_roboto_base_id + 2, ItemClassification.progression),
    ItemName.cartridge_2: GatoRobotoItemData(gato_roboto_base_id + 3, ItemClassification.progression),
    ItemName.cartridge_3: GatoRobotoItemData(gato_roboto_base_id + 4, ItemClassification.progression),
    ItemName.cartridge_4: GatoRobotoItemData(gato_roboto_base_id + 5, ItemClassification.progression),
    ItemName.cartridge_5: GatoRobotoItemData(gato_roboto_base_id + 6, ItemClassification.progression),
    ItemName.cartridge_6: GatoRobotoItemData(gato_roboto_base_id + 7, ItemClassification.progression),
    ItemName.cartridge_7: GatoRobotoItemData(gato_roboto_base_id + 8, ItemClassification.progression),
    ItemName.cartridge_8: GatoRobotoItemData(gato_roboto_base_id + 9, ItemClassification.progression),
    ItemName.cartridge_9: GatoRobotoItemData(gato_roboto_base_id + 10, ItemClassification.progression),
    ItemName.cartridge_10: GatoRobotoItemData(gato_roboto_base_id + 11, ItemClassification.progression),
    ItemName.cartridge_11: GatoRobotoItemData(gato_roboto_base_id + 12, ItemClassification.progression),
    ItemName.cartridge_12: GatoRobotoItemData(gato_roboto_base_id + 13, ItemClassification.progression),
    ItemName.cartridge_13: GatoRobotoItemData(gato_roboto_base_id + 14, ItemClassification.progression),
    ItemName.cartridge_14: GatoRobotoItemData(gato_roboto_base_id + 15, ItemClassification.progression),
}

item_data_table: Dict[str, GatoRobotoItemData] = {
    **modules_item_data_table, 
    **cartidges_item_data_table,
    ItemName.healthkit: GatoRobotoItemData(gato_roboto_base_id + 208, ItemClassification.filler),
    ItemName.progressive_aqueduct: GatoRobotoItemData(gato_roboto_base_id + 237, ItemClassification.progression),
    ItemName.progressive_heater: GatoRobotoItemData(gato_roboto_base_id + 254, ItemClassification.progression),
    ItemName.progressive_vent: GatoRobotoItemData(gato_roboto_base_id + 262, ItemClassification.progression)
}

item_table = {name: data.code for name, data in item_data_table.items()}