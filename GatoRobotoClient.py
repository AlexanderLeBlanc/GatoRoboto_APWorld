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
    print(f"Server Locations: {ctx.server_locations}")
    print(f"Server Locations Size: {len(ctx.server_locations)}")
    ret = await ctx.check_locations([10000])
    print(ret)"""
    
    #while not ctx.exit_event.is_set():
    """Watch game json"""

# Looks like most of these automatically call in the process_server_cmd() method in CommonClient.py
# Not sure if we are overriding it or just executing our own code alongside it
async def process_gatoroboto_cmd(ctx: GatoRobotoContext, cmd: str, args: dict):
    if cmd == "Connected":
        print("CONNECTED SHII")
        
        # Do all file init here
        if not os.path.exists(ctx.save_game_folder):
            os.mkdir(ctx.save_game_folder)
        
        if not os.path.exists(ctx.save_game_folder + "/game_comms.json"):
            game_comms = '{ "cur_message": "", "message_is_stale": "true", "vars_out": { "10408": "false", "11812": "false", "11014": "false", "12314": "false", "10405": "false", "11606": "false", "10417": "false", "11713": "false", "10915": "false", "12413": "false", "10710": "false", "11810": "false", "11214": "false", "11413": "false", "12113": "false", "11106": "false", "10707": "false", "12105": "false", "11119": "false", "10414": "false", "11915": "false", "11613": "false", "10517": "false", "11514": "false", "10814": "false", "10807": "false", "11716": "false", "21716": "false", "12410": "false", "10113": "false", "11114": "false", "11718": "false", "10204": "false", "11503": "false", "11908": "false", "10019": "false", "10313": "false", "10015": "false", "11112": "false", "11122": "false", "10521": "false" }, "vars_in": { "10212": 0, "10211": 0, "10209": 0, "10214": 0, "10210": 0, "10216": 0, "10213": 0, "10215": 0, "10217": 0, "10208": 0, "10237": 0, "10254": 0, "10002": 0 } }'
            game_comms_json = json.loads(game_comms)
            print(str(game_comms_json))
            
            with open(ctx.save_game_folder + "/game_comms.json", 'w') as f:
                json.dump(game_comms_json, f, indent=4)
            
        else:
            """reset state and update from server"""
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
        

