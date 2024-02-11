from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM,CallbackQuery
from pyrogram import Client
from .. import Mukesh
from pyrogram import filters
from ..modules.buttons import *
@Mukesh.on_callback_query(filters.regex("^HELP"))
async def callback_handler(_: Client, query: CallbackQuery):
    try:
        if query.data == "HELP":
            await query.message.edit_text(
                text=HELP,
                reply_markup=IKM(HELP_BACK),
            )     
        elif query.data == "HELP_source":
            await query.message.edit(SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
        elif query.data == "HELP_hurr":
            await query.edit_message_reply_markup(reply_markup=SOURCE_BUTTON)
        elif query.data == "HELP_BACK":
            await query.edit_message_text(START,reply_markup=IKM(MAIN))
        
        
        
        
    except Exception as e:
        print(e)
        await query.message.forward(OWNER_ID)
        await query.message.reply(e)
     
       
      