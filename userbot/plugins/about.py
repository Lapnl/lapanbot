# Ported from other Telegram UserBots for lapnlbot//Made for lapnlbot
# Kangers, don't remove this line 
# @its_Lapnl

"""Available Commands:
.info
"""

import asyncio

from userbot.utils import admin_cmd

@lapnlbot.on(admin_cmd(pattern="info"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "Visit this page to know more about lapnlbot.":
    await event.edit("Thanks")
    animation_chars = [
            "**lapnlbot**",
            "[More Info](https://telegra.ph/Lapnlbot-09-13)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
