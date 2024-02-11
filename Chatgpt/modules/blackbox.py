# -----------CREDITS -----------
# telegram : @python_coderx
# github : noob-mukesh
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from .. import Mukesh
from pyrogram.enums import ChatAction,ParseMode
from config import *
from ..modules.buttons import *

#blackbox
@Mukesh.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def blackbox_chat(bot, message):
    
    try:

        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/blackbox how r u?`")
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://mukesh-api.vercel.app/blackbox?query={a}') 
            x=response.json()["results"]
          
            await message.reply_text(f"{x}\n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True,disable_web_page_preview=True)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")