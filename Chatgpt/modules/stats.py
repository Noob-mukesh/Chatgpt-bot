# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio
from .. import Mukesh
from ..database import *


@Mukesh.on_message(filters.command(["stats", f"tgt@{Mukesh.username}"]))
async def stats(_, m):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await m.reply(f"""  ᴛᴏᴛᴀʟ ꜱᴛᴀᴛꜱ  {Mukesh.mention}:\nᴜꜱᴇʀꜱ: {users}\nᴄʜᴀᴛ: {chats}""")