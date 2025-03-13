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
        get_clean_game_comms_file(ctx.save_game_folder + "/game_comms.json")
        with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
            game_comms = dict(json.load(f))
            
            sending = []
            
            for key in game_comms:
                if str(key).isdigit() and not str(game_comms[str(key)]).isdigit():
                    #print("test: " + str(ctx.missing_locations.__contains__(str(key))) + " // " + str(bool(game_comms[str(key)])))
                    if ctx.missing_locations.__contains__(int(key)) and bool(game_comms[str(key)]):
                        #print("Found an item to send")
                        sending.append(int(key))
            
            if len(sending) != 0:
                "SENDING ITEM YOOO"
                await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sending}])
                        

# Looks like most of these automatically call in the process_server_cmd() method in CommonClient.py
# Not sure if we are overriding it or just executing our own code alongside it
async def process_gatoroboto_cmd(ctx: GatoRobotoContext, cmd: str, args: dict):
    if cmd == "Connected":
        print("CONNECTED SHII")
        
        # Do all file init here
        if not os.path.exists(ctx.save_game_folder):
            os.mkdir(ctx.save_game_folder)
        
        if not os.path.exists(ctx.save_game_folder + "/game_comms.json"):
            game_comms = '{ "cur_message": "", "message_is_stale": {False}, "10408": {False}, "11812": {False}, "11014": {False}, "12314": {False}, "10405": {False}, "11606": {False}, "10417": {False}, "11713": {False}, "10915": {False}, "12413": {False}, "10710": {False}, "11810": {False}, "11214": {False}, "11413": {False}, "12113": {False}, "11106": {False}, "10707": {False}, "12105": {False}, "11119": {False}, "10414": {False}, "11915": {False}, "11613": {False}, "10517": {False}, "11514": {False}, "10814": {False}, "10807": {False}, "11716": {False}, "21716": {False}, "12410": {False}, "10113": {False}, "11114": {False}, "11718": {False}, "10204": {False}, "11503": {False}, "11908": {False}, "10019": {False}, "10313": {False}, "10015": {False}, "11112": {False}, "11122": {False}, "10521": {False}, "10212": {0}, "10211": {0}, "10209": {0}, "10214": {0}, "10210": {0}, "10216": {0}, "10213": {0}, "10215": {0}, "10217": {0}, "10208": {0}, "10237": {0}, "10254": {0}, "10002": {0} }'
            game_comms_json = json.loads(game_comms)
            
            with open(ctx.save_game_folder + "/game_comms.json", 'w') as f:
                json.dump(game_comms_json, f, indent=4)
        else:
            """reset state"""
            get_clean_game_comms_file(ctx.save_game_folder + "/game_comms.json")
            with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
                game_comms_json = dict(json.load(f))
            
                for key in game_comms_json:
                    if str(key).isdigit() and not str(game_comms_json[str(key)]).isdigit():
                        game_comms_json[key] = False
                    elif str(key).isdigit() and str(game_comms_json[str(key)]).isdigit():
                        game_comms_json[key] = 0
                    
                game_comms_json["cur_message"] = ""
                game_comms_json["message_is_stale"] = "true"
                
                f.seek(0)
                f.truncate()
                json.dump(game_comms_json, f, indent=4) 
                
        """update with server values, items get sent in ReceivedItems initially"""
        with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
            game_comms_json = dict(json.load(f))
            for loc in set(args["checked_locations"]):
                game_comms_json[str(loc)] = True
            
            f.seek(0)
            f.truncate()
            json.dump(game_comms_json, f, indent=4)               
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
        if start_index == len(ctx.items_received):
            get_clean_game_comms_file(ctx.save_game_folder + "/game_comms.json")
            with open(ctx.save_game_folder + "/game_comms.json", 'r+') as f:
                game_comms_json = json.load(f)
                
                for item_slot in dict(game_comms_json):
                    if str(game_comms_json[item_slot]).isdigit() and game_comms_json[item_slot] > 0:
                        game_comms_json[item_slot] = 0
                
                for item in args["items"]:
                    net_item = NetworkItem(*item)
                    game_comms_json[str(net_item.item)] = int(game_comms_json[str(net_item.item)]) + 1
                
                f.seek(0)
                f.truncate()
                json.dump(game_comms_json, f, indent=4)

def get_clean_game_comms_file(file_path):
    """
    Reads a JSON file, removes any trailing or embedded null characters (\x00),
    and ensures the file is valid JSON before returning its contents.
    """
    if os.path.exists(file_path):
        with open(file_path, "r+", encoding="utf-8") as f:
            content = f.read()

            # Remove any null characters (\x00) at the end or inside the file
            cleaned_content = content.replace("\x00", "")

            # Only overwrite if changes were made
            if content != cleaned_content:
                f.seek(0)
                f.truncate()
                f.write(cleaned_content)
    else:
        print(f"Error: File does not exist -> {file_path}")
        return None

#Update cartidge ids
#Set up message and stale
#Set up patching
                    
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
        

