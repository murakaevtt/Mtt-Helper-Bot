from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

admin = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Отпр. сообщ.", callback_data="send_message")],
              [InlineKeyboardButton(text="Отпр. оповещ.", callback_data="send_notification")],
              [InlineKeyboardButton(text="Посм. всех польз.", callback_data="view_users")]
    ]
)
