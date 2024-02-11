# -----------CREDITS -----------
# telegram : @python_coderx
# github : noob-mukesh
from pyrogram import filters,Client
from pyrogram.types import CallbackQuery
import asyncio, time
from .. import Mukesh
from config import *
from ..modules.buttons import *
#  callback 

@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )