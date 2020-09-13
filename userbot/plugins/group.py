from userbot.utils import admin_cmd

@lapnlbot.on(admin_cmd(outgoing=True, pattern="group"))
async def join(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("This is my community.\n\n[Channel](http://t.me/giveaways_24hrs)\n\n[Chat Group](https://t.me/giveaways24hrsdiscuss)\n\n[UserBot Tutorial - lapnlbot](https://t.me/lapnlbotHelp)\n\n[lapnlbot Chat](https://t.me/lapnlbotHelpChat)\n\n[Github](https://github.com/Lapnl)\n\n[YouTube](https://bit.ly/adityas7)")
