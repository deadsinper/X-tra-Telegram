"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Collecting All Your data... \n All Your Data is Colleced `", 
            "`Targeted Account Hacked...\n\nPay 10$ To` @mantiz_rip `...Ꮖ ᎻᎪᏙᎬ ᎻᎪᏟᏦᎬᎠ ᎽϴႮᎡ ᎠᎬᏙᏆᏟᎬ... \nᎽϴUᎡ ᏢᎻϴͲϴՏ 𝕒𝕟𝕕 𝕞𝕖𝕕𝕚𝕒Տ ᏔᏆᏞᏞ ᏴᎬ ᏢႮᏴᏞᏆᏟ ᑎᝪᗯ \n\n~~BETTER YOU GIVE THE MONEY~~ \n.WITHIN 2hrs `"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
