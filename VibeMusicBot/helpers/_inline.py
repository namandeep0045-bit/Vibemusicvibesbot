# ==============================================================================
# _inline.py - Inline Buttons
# ==============================================================================

from pyrogram import types


class Inline:
    def __init__(self):
        pass

    def cancel_dl(self, text) -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton(text, callback_data="cancel_download")]
        ]
        return types.InlineKeyboardMarkup(buttons)

    def start_key(self, lang, private=False) -> types.InlineKeyboardMarkup:
        buttons = [
            [
                types.InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ",
                    url="https://t.me/Vibemusicvibes_bot?startgroup=true",
                )
            ],
            [
                types.InlineKeyboardButton(
                    "📚 ᴄᴏᴍᴍᴀɴᴅꜱ",
                    callback_data="help_menu",
                )
            ],
        ]
        return types.InlineKeyboardMarkup(buttons)

    def controls(self, chat_id: int, timer: str = None) -> types.InlineKeyboardMarkup:
        buttons = [
            [
                types.InlineKeyboardButton("⏮", callback_data=f"rewind_{chat_id}"),
                types.InlineKeyboardButton("⏸", callback_data=f"pause_{chat_id}"),
                types.InlineKeyboardButton("⏭", callback_data=f"skip_{chat_id}"),
            ],
        ]

        if timer:
            buttons.append(
                [types.InlineKeyboardButton(timer, callback_data="timer")]
            )

        return types.InlineKeyboardMarkup(buttons)

    def close_button(self) -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton("Close ✖", callback_data="close_menu")]
        ]
        return types.InlineKeyboardMarkup(buttons)

    def ping_markup(self, text) -> types.InlineKeyboardMarkup:
        buttons = [
            [
                types.InlineKeyboardButton(
                    text,
                    url="https://t.me/Vibexmusicbots",
                )
            ]
        ]
        return types.InlineKeyboardMarkup(buttons)
