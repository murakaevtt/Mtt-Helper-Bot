from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from app.methods import get_currency, get_help_txt

import datetime as dt
import math

from aiohttp.web_routedef import route

import app.keyboard as kb
import app.database.requests as rq

helpTxt = get_help_txt()
rt = Router()

class Reg(StatesGroup):
    a = State()
    b = State()
    c = State()
    elo = State()


@rt.message(CommandStart())
async def start(message: Message) -> None:
    await rq.set_user(
        tg_id=int(message.from_user.id),
        first_name=str(message.from_user.first_name),
        last_name=str(message.from_user.last_name),
        is_premium=bool(message.from_user.is_premium),
        is_admin=False
    )
    await message.answer(f"Привет, {message.from_user.first_name}!\nЖми /help", reply_markup=kb.main)


@rt.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(helpTxt, parse_mode="Markdown")
    
    
@rt.message(F.photo)
async def photo_handler(message: Message):
    photo_data = message.photo[-1]
    
    await message.answer(f"{photo_data}")
    

@rt.message(Command("checkcurrencies"))
async def print_currency(message: Message) -> None:
    date = dt.datetime.now().strftime("%d/%m/%Y")
    currencies = get_currency()
    await message.answer(f"Курсы валют на сегодня:\n\nUSD: {currencies["USD"]}₽.\nEUR: {currencies["EUR"]}₽.\nCNY: {currencies["CNY"]}₽.\n\nДата: {date}.")

# Math
#---------------------

@rt.message(Command("solvequadraticequation"))
async def get_a(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.a)
    await message.answer("Введите коэффициент a")


@rt.message(Reg.a)
async def get_b(message: Message, state: FSMContext) -> None:
    await state.update_data(a=message.text)
    await state.set_state(Reg.b)
    await message.answer("Введите коэффициент b")


@rt.message(Reg.b)
async def get_c(message: Message, state: FSMContext) -> None:
    await state.update_data(b=message.text)
    await state.set_state(Reg.c)
    await message.answer("Введите коэффициент c")


@rt.message(Reg.c)
async def print_answer(message: Message, state: FSMContext) -> None:
    await state.update_data(c=message.text)
    data = await state.get_data()
    a, b, c = float(data["a"]), float(data["b"]), float(data["c"])
    discr = b ** 2 - 4 * a * c
    await message.answer("Дискриминант D = %.2f" % discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        await message.answer("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        await message.answer("x = %.2f" % x)
    else:
        await message.answer("Корней нет")
    await state.clear()

# Games
#---------------------

@rt.message(Command("elotorank"))
async def get_elo(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.elo)
    await message.answer("Введите ваш elo")

@rt.message(Reg.elo)
async def print_elo(message: Message, state: FSMContext) -> None:
    await state.update_data(elo=message.text)
    data = await state.get_data()
    elo = int(data["elo"])
    
    if elo < 1000:
        await message.answer("Ело не может быть меньше 1000, запустите команду ещё раз")
    elif elo >= 1000 and elo < 2816:
        await message.answer_photo(photo=str(await rq.get_rank(1)))
    elif elo >= 2816 and elo < 3730:
        await message.answer_photo(photo=str(await rq.get_rank(2)))
    elif elo >= 3730 and elo < 4207:
        await message.answer_photo(photo=str(await rq.get_rank(3)))
    elif elo >= 4207 and elo < 4698:
        await message.answer_photo(photo=str(await rq.get_rank(4)))
    elif elo >= 4698 and elo < 4999:
        await message.answer_photo(photo=str(await rq.get_rank(5)))
    elif elo >= 4999 and elo < 5622:
        await message.answer_photo(photo=str(await rq.get_rank(6)))
    elif elo >= 5622 and elo < 6492:
        await message.answer_photo(photo=str(await rq.get_rank(7)))
    elif elo >= 6492 and elo < 7416:
        await message.answer_photo(photo=str(await rq.get_rank(8)))
    elif elo >= 7416 and elo < 8376:
        await message.answer_photo(photo=str(await rq.get_rank(9)))
    elif elo >= 8376 and elo < 9348:
        await message.answer_photo(photo=str(await rq.get_rank(10)))
    elif elo >= 9348 and elo < 9999:
        await message.answer_photo(photo=str(await rq.get_rank(11)))
    elif elo >= 9999 and elo < 10894:
        await message.answer_photo(photo=str(await rq.get_rank(12)))
    elif elo >= 10894 and elo < 12013:
        await message.answer_photo(photo=str(await rq.get_rank(13)))
    elif elo >= 12013 and elo < 13088:
        await message.answer_photo(photo=str(await rq.get_rank(14)))
    elif elo >= 13088 and elo < 14187:
        await message.answer_photo(photo=str(await rq.get_rank(15)))
    elif elo >= 14187 and elo < 15495:
        await message.answer_photo(photo=str(await rq.get_rank(16)))
    elif elo >= 15495 and elo < 18006:
        await message.answer_photo(photo=str(await rq.get_rank(17)))
    else:
        await message.answer_photo(photo=str(await rq.get_rank(18)))
          
    await state.clear()
