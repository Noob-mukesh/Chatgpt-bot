# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from .. import Mukesh
from pyrogram.enums import ChatAction,ParseMode
from config import *
from ..modules.buttons import *



x=None
#blackbox
@Mukesh.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def blackbox_chat(bot, message):
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/blackbox write simple flask app code`")
    else:
        a = message.text.split(' ', 1)[1]
    # CREDITS
    # TELEGRAM : @Mr_Sukkun
    #  GITHUB : NOOB-MUKESH
    try:
        response = requests.get(f'https://mukesh-api.vercel.app/blackbox?query={a}') 
        if response.status_code==200:
            await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
            x=response.json()["results"]
            
            await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True)  
        else:
            pass

            
    except requests.exceptions.RequestException as e:
        pass
        