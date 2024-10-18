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

mirage_t_type_of_grenade = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="<< Назад <<", callback_data="back")],
        [InlineKeyboardButton(text="Смоки", callback_data="mirage_t_smokes")],
        [InlineKeyboardButton(text="Флешки", callback_data="mirage_t_flashes")],
        [InlineKeyboardButton(text="Молотовы", callback_data="mirage_t_molotov")],
    ]
)

mirage_places_smoke_t = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="<< Назад <<", callback_data="back")],
        [InlineKeyboardButton(text="Смок на сити А", callback_data="mirage_smoke_city")],
        [InlineKeyboardButton(text="Смок на стеирс А", callback_data="mirage_smoke_stairs")],
        [InlineKeyboardButton(text="Смок на джангл и коннектор А", callback_data="mirage_smoke_jungle_conn")],
        [InlineKeyboardButton(text="Смок в коннектор А", callback_data="mirage_smoke_outside_conn")],
        [InlineKeyboardButton(text="Смок в окно мид", callback_data="mirage_smoke_window")],
        [InlineKeyboardButton(text="Смок на старт мид", callback_data="mirage_smoke_start_mid")],
        [InlineKeyboardButton(text="Смок на арки Б", callback_data="mirage_smoke_arches_b")],
        [InlineKeyboardButton(text="Смок в окно кухни Б", callback_data="mirage_smoke_window_kitchen")],
        [InlineKeyboardButton(text="Смок на выход кухни Б", callback_data="mirage_smoke_kitchen")]
    ]
)
