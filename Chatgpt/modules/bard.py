# -----------CREDITS -----------
# telegram : @python_coderx
# github : noob-mukesh
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup
import asyncio, time,requests
from .. import Mukesh
from config import *
from ..modules.buttons import *
#  bard 

@Mukesh.on_message(filters.command(["bard"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def bard_chat(bot, message):
    
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/bard write code for fetching api?`")
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://mukesh-api.vercel.app/bard?query={a}') 
            x=response.json()["results"]
        
            await message.reply_text(f"{x}\n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")