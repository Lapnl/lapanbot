# Copyright lapnlbot
# For @lapnlbotHelp coded by @Lapnl
# Kangers keep credits else I'll take down 🧐

import sys
from telethon import events, functions, version, __version__
import random
from userbot.utils import register
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "lapnlbot User"

ONLINESTR = [
	"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**lapnlbot is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Aditya 🇮🇳](tg://user?id=719195224) \n\n**More help -** @lapnlbotHelpChat \n\n           [🚧 GitHub Repository 🚧](https://github.com/Lapnl/lapnlbot)",
	f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to lapnlbot**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @lapnlbotHelpChat \n\n✔️ Created by: [Aditya 🇮🇳](tg://user?id=719195224) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/Lapnl/lapnlbot)"
]

@lapnlbot.on(admin_cmd(outgoing=True, pattern="online"))
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(random.choice(ONLINESTR))
