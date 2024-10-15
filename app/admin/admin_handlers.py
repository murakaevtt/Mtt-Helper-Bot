from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from aiohttp.web_routedef import route

import app.keyboard as kb
import app.admin.admin_keyboard as admin_kb
import app.database.requests as rq

admin_router = Router()

class Reg(StatesGroup):
    id = State()

@admin_router.message(Command("admin"))
async def admin(message: Message) -> None:
    if await rq.get_user_rank(message.from_user.id):
        await message.answer("Добро пожаловать в админ панель!", reply_markup=admin_kb.admin)
    else:
        await message.answer("Вы не являетесь администратором")


@admin_router.callback_query(F.data == "view_users")
async def view_users(message: Message):
    for i in range(2):
        await message.answer(f"Name: {rq.view_users(i).f_name} ID: {rq.view_users(i).user}")
        
@admin_router.callback_query(F.data == "send_message")
async def get_id(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.id)
    await message.answer("Введите ID")
   
@admin_router.message(Reg.id)
async def send_message(message: Message, state: FSMContext) -> None:
    await state.update_data(id=message.text)