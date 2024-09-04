from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import app.keyboards as akb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        f"Hello! Your id is {message.from_user.id}, your name is {message.from_user.first_name}",
        reply_markup=akb.setting_start,
    )


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Ok, I'll help you!")


@router.message(F.text == "как дела?")
async def how_are_you(message: Message):
    await message.answer("I'm fine!")


@router.message(F.photo)
async def put_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMcZtjMy26vPbfroH8AARPU1Ddda9NSAAJH3DEblfbISjXP69tnC-_fAQADAgADeAADNgQ",
        caption="This is code!",
    )
