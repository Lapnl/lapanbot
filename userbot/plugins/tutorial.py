"""Plugin to get the video tutorial to deploy lapnlbot
.tut"""

from userbot.utils import register
from userbot.utils import admin_cmd

@lapnlbot.on(admin_cmd(outgoing=True, pattern="tut"))

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("Get a userbot like mine!! Watch [this video tutorial](https://youtu.be/XmvdDHiIDb4) on deploying...")
