from __future__ import annotations
import os
import sys
import asyncio
import typing
import bsdiff4
import shutil
import json

import Utils

from NetUtils import NetworkItem, ClientStatus
from worlds import gatoroboto
from MultiServer import mark_raw
from CommonClient import CommonContext, server_loop, \
    gui_enabled, ClientCommandProcessor, logger, get_base_parser
from Utils import async_start

"""
Notes on things ive learned:
locations_checked = list maintained by client of locations youve checked
checked_locations = list from server of locations youve checked
"""

class GatoRobotoCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx) 

class GatoRobotoContext(CommonContext):
    tags = {"AP", "Online"}
    game = "Gato Roboto"
    command_processor = GatoRobotoCommandProcessor
    save_game_folder = os.path.expandvars(r"%localappdata%/GatoRoboto")
    checks_to_consume = []
    
    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game = "Gato Roboto"
        self.syncing = False
        
        # Magical item handling value that I don't understand
        self.items_handling = 0b111
        
        # self.save_game_folder: Files go in this path to pass data between us and the actual game
        self.save_game_folder = os.path.expandvars(r"%localappdata%/GatoRoboto")

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd, args):
        print('SOMETHING: ' + str(cmd))
        
        if (cmd == 'Connected'):
            print('HELL YEE')
            self.game = self.slot_info[self.slot].game
        
        async_start(process_gatoroboto_cmd(self, cmd, args))
        
    async def connect(self, address: typing.Optional[str] = None):
        print('log connect')
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        print('log disconnect')
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        print('log connect close')
        await super().connection_closed()

    async def shutdown(self):
        print('log shutdown')
        await super().shutdown()
        
    def run_gui(self):
        from kvui import GameManager

        class UTManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Gato Roboto Client"

        self.ui = UTManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")
        
async def game_watcher(ctx: GatoRobotoContext):
    """placeholder"""
    """await asyncio.sleep(20)
    print("starting send")
    #while not ctx.exit_event.is_set():
    ret = await ctx.check_locations([10408])
    print(ret)"""
    
    while not ctx.exit_event.is_set():
        await asyncio.sleep(0.1)
        """Watch game json"""
        if os.path.exists(ctx.save_game_folder + "/game_comms.json"):
            with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
                game_comms = get_clean_game_comms_file(f)
                
                sending = []
                
                for key in game_comms:
                    if str(key).isdigit() and not str(game_comms[str(key)]).isdigit():
                        #print("test: " + str(ctx.missing_locations.__contains__(str(key))) + " // " + str(bool(game_comms[str(key)])))
                        if ctx.missing_locations.__contains__(int(key)) and int(game_comms[str(key)]) > 0:
                            #print("Found an item to send")
                            sending.append(int(key))
                
                if len(sending) != 0:
                    "SENDING ITEM YOOO"
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sending}])

                f.close()
                        

# Looks like most of these automatically call in the process_server_cmd() method in CommonClient.py
# Not sure if we are overriding it or just executing our own code alongside it
async def process_gatoroboto_cmd(ctx: GatoRobotoContext, cmd: str, args: dict):
    if cmd == "Connected":
        print("CONNECTED SHII")
        
        # Do all file init here
        if not os.path.exists(ctx.save_game_folder):
            os.mkdir(ctx.save_game_folder)
        
        #Check if exists, if it doesnt make a json
        if not os.path.exists(ctx.save_game_folder + "/game_comms.json"):
            game_comms = { 
                "cur_message": "", 
                "message_is_stale": 1,
                "current_item_index": "",
                "prev_item_index": "",  
                "10408": 0, 
                "11812": 0, 
                "11014": 0, 
                "12314": 0, 
                "10405": 0, 
                "11606": 0, 
                "10417": 0, 
                "11713": 0, 
                "10915": 0, 
                "12413": 0, 
                "10710": 0, 
                "11810": 0, 
                "11214": 0, 
                "11413": 0, 
                "12113": 0, 
                "11106": 0, 
                "10707": 0, 
                "12105": 0, 
                "11119": 0, 
                "10414": 0, 
                "11915": 0, 
                "11613": 0, 
                "10517": 0, 
                "11514": 0, 
                "10814": 0, 
                "10807": 0, 
                "11716": 0, 
                "21716": 0, 
                "12410": 0, 
                "10113": 0, 
                "11114": 0, 
                "11718": 0, 
                "10204": 0, 
                "11503": 0, 
                "11908": 0, 
                "10019": 0, 
                "10313": 0, 
                "10015": 0, 
                "11112": 0, 
                "11122": 0, 
                "10521": 0, 
                "10212": 0, 
                "10211": 0, 
                "10209": 0, 
                "10214": 0, 
                "10210": 0, 
                "10216": 0, 
                "10213": 0, 
                "10215": 0, 
                "10217": 0, 
                "10208": 0, 
                "10237": 0, 
                "10254": 0, 
                "10262": 0 
            }
            game_comms_json = json.dumps(game_comms, indent=4)
            
            with open(ctx.save_game_folder + "/game_comms.json", 'w') as f:
                f.write(game_comms_json)
                f.close()
        #Check if exists, if it does restore json to initial values, don't mark as dirty yet
        else:
            """reset state"""
            with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
                game_comms_json = get_clean_game_comms_file(f)
            
                for key in game_comms_json:
                    if str(key).isdigit():
                        game_comms_json[key] = 0
                    
                game_comms_json["cur_message"] = ""
                game_comms_json["message_is_stale"] = 0
                
                f.seek(0)
                f.truncate()
                json.dump(game_comms_json, f, indent=4) 
                f.close()
                
        """update with server values, items get sent in ReceivedItems initially"""        
        with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
            game_comms_json = get_clean_game_comms_file(f)
            for loc in set(args["checked_locations"]):
                game_comms_json[str(loc)] = 1
            
            f.seek(0)
            f.truncate()
            json.dump(game_comms_json, f, indent=4)   
            f.close()    
    elif cmd == "RoomInfo":
        # Probably not necessary from looking at other clients
        print("Info: " + str(ctx.seed_name) + " : " + str(args["seed_name"]))
    elif cmd == "LocationInfo":
        # Potentially for hinting?
        print("Loc. Info: " + str(args["locations"]))
    elif cmd == "RoomUpdate":
        # Update checked locations in files for game
        print("Room Updates")
    elif cmd == "ReceivedItems":
        # Big logical state machine to track item index into what item gets written to file
        print("GOT SOME ITEMS")
        print(str(args["items"]))
        ctx.watcher_event.set()
        
        start_index = args["index"]
        
        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{"cmd": "Sync"}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
        
        #if 
        if start_index == len(ctx.items_received):
            if os.path.exists(ctx.save_game_folder + "/game_comms.json"):
                with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
                    game_comms_json = get_clean_game_comms_file(f)
                    
                    game_comms_json["current_item_index"] = str(start_index)
                    
                    for item_slot in dict(game_comms_json):
                        if str(game_comms_json[item_slot]).isdigit() and game_comms_json[item_slot] > 0:
                            game_comms_json[item_slot] = 0
                    
                    for item in args["items"]:
                        net_item = NetworkItem(*item)
                        game_comms_json[str(net_item.item)] = int(game_comms_json[str(net_item.item)]) + 1
                    
                    f.seek(0)
                    f.truncate()
                    json.dump(game_comms_json, f, indent=4)
                    
                    f.close()
            

import os
import json

def get_clean_game_comms_file(f):
    """
    Reads a JSON file, removes any trailing or embedded null characters (\x00),
    and ensures the file is valid JSON before saving the cleaned version.
    """
    content = f.read()

    cleaned_content = content.replace("\x00", "").strip()

    if not cleaned_content.endswith("}"):
        cleaned_content += "}"

    try:
        cleaned_json = json.loads(cleaned_content)
    except json.JSONDecodeError:
        print("Error: Invalid JSON file, unable to fix.")
        return
    
    if content != cleaned_content:
        f.seek(0)
        f.truncate()
        f.write(cleaned_content)
        print("JSON file cleaned successfully.")
        
    return cleaned_json

#Update cartidge ids
#Set up message and stale
#Set up patching
#fix yaml gen
#make mrkdown for webworld
#fix json gen
                    
def main():
    Utils.init_logging("GatoRobotoClient", exception_logger="Client")

    async def _main():
        ctx = GatoRobotoContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        asyncio.create_task(
            game_watcher(ctx), name="GatoRobotoProgressionWatcher")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()

parser = get_base_parser(description="Gato Roboto Client, for text interfacing.")
args = parser.parse_args()
main()
        

