"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @mantiz_rip"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`MANTIS KA PERO BOT ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @mantiz_rip\n"
                     "`Bot created by:` [MANTIS]\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[🤑🤑🤑🤑🤑🤑🤑]")
