from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),
            InlineKeyboardButton(
                text="Sᴜᴘᴘᴏʀᴛ",
                url=f"https://t.me/{SUPPORT_GROUP}",
            )
        ],
        ]
    return buttons

def private_panel(_):
     buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="settings_back_helper")
        ],
        [
            InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", callback_data="support"),
            InlineKeyboardButton(text="Sᴏᴜʀᴄᴇ", callback_data="gib_source")
        ]
    ]
    return buttons
