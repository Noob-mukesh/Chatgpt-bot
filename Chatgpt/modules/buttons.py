
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import *
from random import choice
from .. import Mukesh

import requests

def send():
    headers = {"accept": "application/json"}
    response = requests.get("https://mukesh-api.vercel.app/base/decode?query=aHR0cHM6Ly9naXRodWIuY29tL05vb2ItbXVrZXNoL0NoYXRncHQtYm90", headers=headers)
    return response.json()["results"]
xy=send()  

START = f""" <b>
๏ ʜᴇʏ, ɪ ᴀᴍ <a href="https://t.me/{Mukesh.username}"> {Mukesh.name} </a>

➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴀɴᴅ ᴄᴀɴ 
ᴀɴsᴡᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀɪᴇs ᴇᴀsʟɪʏ
──────────────────
Rᴇᴀᴅ Tʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ

Pᴏᴡᴇʀᴇᴅ Bʏ @Mr_Sukkun  </b>"""
SOURCE_TEXT = f"""<b>
๏ ʜᴇʏ, ɪ ᴀᴍ <a href="https://t.me/{Mukesh.username}"> {Mukesh.name} </a>
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ</b>
"""
HELP = f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {Mukesh.mention}
**➻ ᴜsᴀɢᴇ** /chatgpt <prompt> ᴇxᴀᴍᴘʟᴇ: `/chatgpt write shorts notes of electricity`
**➻ ᴜsᴀɢᴇ** /bard <prompt> ᴇxᴀᴍᴘʟᴇ: `/bard write a simple flask app in python.`
**➻ ᴜsᴀɢᴇ** /blackbox <prompt> ᴇxᴀᴍᴘʟᴇ: `/blackbox write a simple website using python.`
**➻ ᴜsᴀɢᴇ** /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.

"""

x = ["❤️", "🎉", "✨", "🪸", " 🎉 ", " 🎈 ", "🎯"]
g = choice(x)


MAIN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),
    ],
    [
        IKB(text="ʜᴇʟᴘs", callback_data="HELP"),
    ],
    [
        IKB(text="sᴏᴜʀᴄᴇ ", callback_data="HELP_source"),
        
        IKB(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
]
]

PNG_BTN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),
    ],
    [
        IKB("sᴜᴘᴘᴏʀᴛ",
            url=f"https://t.me/{SUPPORT_GRP}",
        ),
    ],
]
gpt_button = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),

        IKB("ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID)
    ],
]



HELP_BACK = [

    [
        IKB("ʙᴀᴄᴋ", callback_data="HELP_BACK"),
    ],
]

SOURCE_BUTTONS = IKM(
    [
        [IKB("sᴏᴜʀᴄᴇ", callback_data="HELP_hurr")],
        [
            IKB(" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
            IKB(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK")
        ]
    ]
)
SOURCE_BUTTON = IKM(
    [
        [IKB("sᴏᴜʀᴄᴇ" ,url=xy)
        ]
    ]
)