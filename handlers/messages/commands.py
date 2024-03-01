from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app import bot, dp

@dp.message()
async def echo_handler2(message: types.Message) -> None:
    # запрос к базе данных длительностью 500 мс
    response = await message.answer(
        f'Hello! Your name is {message.from_user.full_name} and id is {message.from_user.id}',
        disable_notification=True,
        protect_content=True,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                          [[InlineKeyboardButton(text='Youtube', callback_data='1')],[InlineKeyboardButton(text='Youtube', callback_data='1')],
                                           [[InlineKeyboardButton(text='Youtube', callback_data='1')]]
                                           ]),

    )



    print()
