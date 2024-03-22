# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup
import asyncio, time,requests
from .. import Mukesh
from config import *
from ..modules.buttons import *
#  bard 
from MukeshAPI import api
x=None
@Mukesh.on_message(filters.command(["bard"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def bard_chat(bot, message):
    global x
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/bard write shorts notes on human eyes`")
    else:
        a = message.text.split(' ', 1)[1]
    
    try:
        response =api.gemini(a)
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        x=response["results"]
        
        await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True)  
        else:
            pass

            
    except requests.exceptions.RequestException as e:
        pass
        
