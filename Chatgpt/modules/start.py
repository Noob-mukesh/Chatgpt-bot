# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio
from .. import Mukesh
from ..modules.buttons import *
from Chatgpt.database import *
from pyrogram.enums import ChatType, ParseMode

@Mukesh.on_message(filters.command(["start", f"start@{Mukesh.username}"]))
async def start(_, m):
    accha = await m.reply_text(f"{g}")
    await asyncio.sleep(0.2)
    await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
    await asyncio.sleep(0.2)
    await accha.delete()
    await asyncio.sleep(0.4)
    await m.reply_photo(
        START_IMG, caption=START, parse_mode=ParseMode.HTML, reply_markup=IKM(MAIN)
    )

    try:
        if m.chat.type == ChatType.PRIVATE:
            await save_id(m.from_user.id)
        else:
            await chat_id(m.chat.id)
    except Exception as e:
        await m.reply(e)