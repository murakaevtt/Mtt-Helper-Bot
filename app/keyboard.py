from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/help")]],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню...",
)
