from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Catalog")],
        [KeyboardButton(text="Basket"), KeyboardButton(text="Contacts")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Select a menu item.",
)

setting_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="You can watch the video here!", url="https://www.youtube.com/"
            )
        ]
    ]
)
