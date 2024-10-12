import asyncio, logging, os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import rt
from app.database.models import async_main

log = False


async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(rt)
    if logging:
        logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
