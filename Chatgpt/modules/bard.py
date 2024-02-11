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
x=None
@Mukesh.on_message(filters.command(["bard"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def bard_chat(bot, message):
    global x
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/bard write simple flask app using python?`")
    else:
        a = message.text.split(' ', 1)[1]
    
    try:
        
        response = requests.get(f'https://mukesh-api.vercel.app/bard?query={a}') 
        if response.status_code==200:
            x=response.json()["results"]
            
    except requests.exceptions.RequestException as e:

        response = requests.get(f'https://mukesh-api.vercel.app/chatgpt?query={a}') 
        if response.status_code==200:
            x=response.json()["results"]
        # CREDITS
        # TELEGRAM : @Mr_Sukkun
        #  GITHUB : NOOB-MUKESH
    except requests.exceptions.RequestException as e:
        response = requests.get(f'https://mukesh-api.vercel.app/blackbox?query={a}') 
        if response.status_code==200:
            x=response.json()["results"]
    finally:
        await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True)  