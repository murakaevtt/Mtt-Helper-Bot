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
import app.admin.admin_keyboard as admin_kb
import app.database.requests as rq

helpTxt = get_help_txt()
router = Router()


class Reg(StatesGroup):
    a = State()
    b = State()
    c = State()
    elo = State()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await rq.set_user(
        tg_id=int(message.from_user.id),
        first_name=str(message.from_user.first_name),
        last_name=str(message.from_user.last_name),
        is_premium=bool(message.from_user.is_premium),
        is_admin=False,
    )
    await message.answer(
        f"Привет, {message.from_user.first_name}!\nЖми /help", reply_markup=kb.main
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(helpTxt, parse_mode="Markdown")


@router.message(F.photo)
async def photo_handler(message: Message):
    photo_data = message.photo[-1]

    await message.answer(f"{photo_data}")


@router.message(Command("checkcurrencies"))
async def print_currency(message: Message) -> None:
    date = dt.datetime.now().strftime("%d/%m/%Y")
    currencies = get_currency()
    await message.answer(
        f"Курсы валют на сегодня:\n\nUSD: {currencies['USD']}₽.\nEUR: {currencies['EUR']}₽.\nCNY: {currencies['CNY']}₽.\n\nДата: {date}."
    )


# Math
# ---------------------


@router.message(Command("solvequadraticequation"))
async def get_a(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.a)
    await message.answer("Введите коэффициент a")


@router.message(Reg.a)
async def get_b(message: Message, state: FSMContext) -> None:
    await state.update_data(a=message.text)
    await state.set_state(Reg.b)
    await message.answer("Введите коэффициент b")


@router.message(Reg.b)
async def get_c(message: Message, state: FSMContext) -> None:
    await state.update_data(b=message.text)
    await state.set_state(Reg.c)
    await message.answer("Введите коэффициент c")


@router.message(Reg.c)
async def print_answer(message: Message, state: FSMContext) -> None:
    await state.update_data(c=message.text)
    data = await state.get_data()
    a, b, c = float(data["a"]), float(data["b"]), float(data["c"])
    discr = b**2 - 4 * a * c
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
# ---------------------
# CS2 -------------------------------------------------------------------------------------------------------


@router.message(Command("elotorank"))
async def get_elo(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.elo)
    await message.answer("Введите ваш elo")


@router.message(Reg.elo)
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


@router.message(Command("raskid"))
async def choose_map(message: Message):
    await message.answer("Выберите карту", reply_markup=kb.cs_map)


@router.callback_query(F.data == "back")
async def back(query: CallbackQuery):
    await query.message.edit_text(text="Выберите карту", reply_markup=kb.cs_map)
    await query.answer("Вы вернулись в начало меню")


@router.callback_query(F.data == "mirage")    
async def choose_side(query: CallbackQuery):
    await query.answer("Вы выбрали мираж\nВся информация взята с сайта: https://profilerr.net/ru/raskidki-na-karte-mirage-v-cs-2-smoki-fleshki-molotovy/")
    await query.message.edit_text(text="Выберите сторону", reply_markup=kb.mirage_cs_side)
    

@router.callback_query(F.data == "mirage_t_side")
async def mirage_t_side(query: CallbackQuery):
    await query.answer("Вы выбрали т-сторону")
    await query.message.edit_text(text="Выберите вариант раскида", reply_markup=kb.mirage_t_type_of_grenade)


@router.callback_query(F.data == "mirage_ct_side")
async def mirage_ct_side(query: CallbackQuery):
    await query.answer("Вы выбрали кт-сторону")
    await query.message.edit_text(text="Выберите вариант раскида", reply_markup=kb.mirage_ct_type_of_grenade)


# Mirage Terrorist smokes -----------------------------------------------------------------------------------


@router.callback_query(F.data == "mirage_t_smokes")
async def mirage_t_smokes(query: CallbackQuery):
    await query.answer("Вы выбрали смоки")
    await query.message.edit_text(text="Выберите место", reply_markup=kb.mirage_places_smoke_t)


@router.callback_query(F.data == "mirage_smoke_city")
async def mirage_smoke_city(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок на сити")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(1)), caption="Становимся в упор к металлическому перилу. Ориентиром будет вот этот угол на стенке. Используйте jumpthrow, как только будете готовы.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(2)), caption="Смок идеально закроет КТ. Вы можете не опасаться, что игрок сможет залезть на ящик, так как этот нюанс смок также с легкостью контрит.")


@router.callback_query(F.data == "mirage_smoke_stairs")
async def mirage_smoke_stairs(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок на стеирс")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(3)), caption="Поднявшись наверх в рампе террористов, упритесь в среднюю балку на стене.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(4)), caption="Здесь очень нетипичный ориентир. Может показаться, что я просто навелся в небо, но, посмотрев ниже, можно увидеть, что от значка террористов идет белая линия, которую нужно выровнять по левому углу этого выступа.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(5)), caption="Смок на стеирс Мираж КС 2 (на голову) идеально закрывает ступеньки и еще немного просмотр плента с кона, не перекрывая при этом место, где любят прятаться противники при обычном смоке на стеирс.")


@router.callback_query(F.data == "mirage_smoke_jungle_conn")
async def mirage_smoke_jungle_conn(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок на джангл+конн")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(6)), caption="Позиция почти та же, что и для смока стеирс, но немного левее вы можете увидеть деревянную доску, ориентиром будет вот эта черная линия.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(7)), caption="Развернувшись, наведитесь на серую точку на этом выступе и киньте смок без прыжка.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(8)), caption="Этот смок ложится немного глубже, чем дефолтный, не выступая при этом на лавочку, что создавало небольшой ванвей для кт-шников.")
    

@router.callback_query(F.data == "mirage_smoke_outside_conn")
async def mirage_smoke_outside_conn(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок в коннектор")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(9)), caption="Становитесь перед урной на респауне. Также отсюда дают дым в окно на Мираже в КС 2.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(10)), caption="Сидя, прицельтесь на правый верхний угол этого окна и начинайте ползти вперед.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(11)), caption="Когда ваш прицел спустится к началу ковра, нажмите jumpthrow.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(12)), caption="Смок в кон на Мираже КС 2 идеально ложится, перекрывая вижн с А-плента, и позволяет вам занять кон или сделать сплит через шорт.")
    

@router.callback_query(F.data == "mirage_smoke_window")
async def mirage_smoke_window(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок в окно")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(13)), caption="Основной смок на этой мапе – дым в окно Мираж КС 2. Позиция все та же, что и для смока в кон.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(14)), caption="Наведитесь немного левее от края большой серой полосы и, зажав “D”, киньте смок с jumpthrow.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(15)), caption="Эти смоки в окно на мираже КС 2 попадают ровно в середину и прекрасно перекрывают вид для занятия мидла.")
    

@router.callback_query(F.data == "mirage_smoke_start_mid")
async def mirage_smoke_start_mid(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок на старт мида")
    await callback.message.answer("Для этого смока нужно залезть на верх мусорной урны.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(16)), caption="Прицелившись на правый край антенны, просто киньте смок с помощью ЛКМ.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(17)), caption="Этот смок очень вариативен, под него вы можете пробежать за ящики или, прицелившись, попросить тиммейта взорвать его, застав при этом игрока в окне врасплох.")
    

@router.callback_query(F.data == "mirage_smoke_arches_b")
async def mirage_smoke_arches_b(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок на арки Б")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(18)), caption="Кидаются они вот с этих двух позиций. При идеальном раскладе эту раскидку должны выполнять синхронно два игрока.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(19)), caption="Правая арка дается с левой стороны. Выровняйте доску так, чтобы она перекрывала только половину окна, затем прицельтесь на выступ крыши и нажмите jumpthrow.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(20)), caption="Этот смок на эдвард обезопасит вас от возможного кросфаера со стороны оппонентов.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(21)), caption="Левая арка дается справа. Найдите на стене белое пятно на коричневом фоне и нажмите jumpthrow.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(22)), caption="Смоки отрезают игрока шорта, при выходе вам всего-то нужно разобраться с опорником Б и поставить бомбу.")
    

@router.callback_query(F.data == "mirage_smoke_window_kitchen")
async def mirage_smoke_window_kitchen(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок на окно кухни")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(23)), caption="Займите этот угол в Б-апартаментах.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(24)), caption="Наведитесь на верхний выступ башни и с помощью jumpthrow киньте смок.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(25)), caption="Этот смок на китчен залетает в середину окна и не сильно выпирает наружу, позволяя увидеть соперника, если тот захочет выпрыгнуть за плент.")
    

@router.callback_query(F.data == "mirage_smoke_kitchen")
async def mirage_smoke_kitchen(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок на выход кухни")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(26)), caption="Также с этой позиции прицельтесь на выступ между двумя окнами — jumpthrow и смок в мейне.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(27)))


# Mirage Counter-Terrorist smokes -----------------------------------------------------------------------------------


@router.callback_query(F.data == "mirage_ct_smokes")
async def mirage_t_smokes(query: CallbackQuery):
    await query.answer("Вы выбрали смоки")
    await query.message.edit_text(text="Выберите место", reply_markup=kb.mirage_places_smoke_ct)


@router.callback_query(F.data == "mirage_smoke_pit")
async def mirage_smoke_pit(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок в яму")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(28)), caption="Упритесь спиной в металлические трубы.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(29)), caption="Развернувшись, прицельтесь немного выше надписей на ящике и киньте смок с ЛКМ.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(30)), caption="Яма идеально закрыта без щелей, только опасайтесь умников, которые любят выйти в смок, занимая тетрис.")
    

@router.callback_query(F.data == "mirage_smoke_conn")
async def mirage_smoke_conn(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок в коннектор")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(31)), caption="Каждый игрок коннектора должен знать этот смок. На начале раунда киньте смок немного левее этого выступа на стене шорта. Довольно сложно кинуть его правильно с первого раза, но спустя несколько попыток у вас однозначно получится.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(32)), caption="Смок создаст вам небольшой ванвей, а также потушит молотов, который часто дают игроки атаки.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(33)), caption="Примерно так он выглядит от лица атаки. Довольно сложно увидеть вас, не правда ли?")


@router.callback_query(F.data == "mirage_smoke_palace")
async def mirage_smoke_palace(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок в палас")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(34)), caption="Становимся в угол на выходе из кухни.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(35)), caption="Наведитесь посередине края правого окна и киньте смок с помощью jumpthrow.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(36)))


@router.callback_query(F.data == "mirage_smoke_mid")
async def mirage_smoke_mid(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок закрывающий вход на мид")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(37)), caption="На начале раунда станьте в этот угол и проинформируйте тиммейтов о своем плане.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(38)), caption="Прицельтесь на начало антенны и, зажав кнопку “D”, начинайте бежать.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(39)), caption="Когда ваш прицел будет примерно на середине, не сбавляя темп, нажмите jumpthrow.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(40)), caption="Граната стабильно прилетает в мид, не давая собрать террористам информацию и затрудняя их выход.")


@router.callback_query(F.data == "mirage_smoke_ups")
async def mirage_smoke_ups(callback: CallbackQuery):
    await callback.answer("Вы выбрали смок в апсы")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(41)), caption="При выходе из мейна упритесь в мусорный бак.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(42)), caption="Прицельтесь немного левее серой точки на зеленом брезенте — нажмите ЛКМ.")
    await callback.message.answer_photo(photo=str(await rq.get_mirage_links(43)))
    