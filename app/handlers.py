from io import BytesIO

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# import app.keyboards as akb
from app.clients_setup import upload_to_s3
from bot_config import bot

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        f"Hello, {message.from_user.first_name}! Send me your selfie :)",
        # reply_markup=akb.setting_start,
    )


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Ok, I'll help you!")


@router.message(F.text == "как дела?")
async def how_are_you(message: Message):
    await message.answer("I'm fine!")


@router.message(F.photo)
async def put_photo(message: Message):
    selfie = message.photo[-1]
    file_id = selfie.file_id
    file_info = await bot.get_file(file_id)

    # Получаем путь к файлу
    file_path = file_info.file_path

    # Скачиваем файл с Telegram
    file = await bot.download_file(file_path)

    # Используем BytesIO для хранения данных в памяти
    file_in_memory = BytesIO(file.getvalue())

    # Загружаем в S3
    upload_to_s3(file_in_memory, f"telegram_selfie/{file_id}.jpg")

    await message.answer(f"ID photo: {message.photo[-1].file_id}")


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMcZtjMy26vPbfroH8AARPU1Ddda9NSAAJH3DEblfbISjXP69tnC-_fAQADAgADeAADNgQ",
        caption="This is code!",
    )
