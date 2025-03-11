from __future__ import annotations
import os
import sys
import asyncio
import typing
import bsdiff4
import shutil

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
    save_game_folder = os.path.expandvars(r"%localappdata%/UNDERTALE")
    
    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game = "Gato Roboto"
        self.syncing = False
        
        # self.save_game_folder: files go in this path to pass data between us and the actual game
        self.save_game_folder = os.path.expandvars(r"%localappdata%/UNDERTALE")
        
    def on_package(self, cmd, args):
        print('SOMETHING: ' + str(cmd))
        
        if (cmd == 'Connected'):
            print('HELL YEE')
        
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
    await asyncio.sleep(20)
    print("starting send")
    #while not ctx.exit_event.is_set():
    print(f"Server Locations: {ctx.server_locations}")
    print(f"Server Locations Size: {len(ctx.server_locations)}")
    ret = await ctx.check_locations([10000])
    print(ret)
    #await ctx.send_msgs([{"cmd": "LocationChecks", "locations": [10000]}])
        #print("Sent Items: " + str(rply))
        
async def process_gatoroboto_cmd(ctx: GatoRobotoContext, cmd: str, args: dict):
    if cmd == "Connected":
        print("CONNECTED SHII")
    if cmd == "RoomInfo":
        print("Info: " + str(ctx.seed_name) + " : " + str(args["seed_name"]))
    if cmd == "ReceivedItems":
        print("GOT SOME ITEMS")
        print(str(args["items"]))
        
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
        

