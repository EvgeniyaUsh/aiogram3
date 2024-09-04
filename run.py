import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router as app_router
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(app_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
