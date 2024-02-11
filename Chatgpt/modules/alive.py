# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio, time
from .. import Mukesh
from config import START_IMG
from ..modules.buttons import *



@Mukesh.on_message(
    filters.command(["ping", "alive"], prefixes=["+", "/", "-", "?", "$", "&", "."])
)
async def ping(_, message):
    start = time.time()
    t = "__ᴘɪɴɢɪɴɢ...__"
    txxt = await message.reply(t)
    await asyncio.sleep(0.25)
    await txxt.edit_text("__ᴘɪɴɢɪɴɢ.....__")
    await asyncio.sleep(0.35)
    await txxt.delete()
    end = time.time()
    ms = str(round((end - start) * 1000, 3)) + " ᴍs"
    await message.reply_photo(
        photo=START_IMG,
        caption=f"ʜᴇʏ ʙᴀʙʏ!!\n{Mukesh.mention} ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ {ms} \n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ  @mr_sukkun**",
        reply_markup=IKM(PNG_BTN),
    )