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

cs_map = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="<< Назад <<", callback_data="back")],
        [InlineKeyboardButton(text="Mirage", callback_data="mirage")],
    ]
)

mirage_cs_side = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="<< Назад <<", callback_data="back")],
        [InlineKeyboardButton(text="T", callback_data="mirage_t_side")],
        [InlineKeyboardButton(text="CT", callback_data="mirage_ct_side")],
    ]
)

mirage_raskid_t = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="<< Назад <<", callback_data="back")],
        [InlineKeyboardButton(text="Смок на сити", callback_data="mirage_smoke_city")],
        [InlineKeyboardButton(text="Смок на стеирс", callback_data="mirage_smoke_stairs")],
    ]
)
