# -----------CREDITS -----------
# telegram : @python_coderx
# github : noob-mukesh
from pyrogram import filters
import asyncio, time
from .. import Mukesh
from config import *
from ..modules.buttons import *
from pyrogram.types import InlineKeyboardMarkup
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)