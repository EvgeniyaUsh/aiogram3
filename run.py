import asyncio
import logging

from app.handlers import router as app_router
from bot_config import bot, dp


async def main():
    dp.include_router(app_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
