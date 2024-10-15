import asyncio, logging, os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router
from app.admin.admin_handlers import admin_router
from app.database.models import async_main

log = True


async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(admin_router)
    if log:
        logging.basicConfig(level=logging.INFO)
    await bot.send_message(1046345341, "Бот включен ✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
