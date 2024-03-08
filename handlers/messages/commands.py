from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app import bot, dp

@dp.message()
async def echo_handler2(message: types.Message) -> None:
    # запрос к базе данных длительностью 500 мс
    # response = await message.answer(
    #     f'Hello! Your name is {message.from_user.full_name} and id is {message.from_user.id}',
    #     reply_markup=InlineKeyboardMarkup(inline_keyboard=
    #                                       [[InlineKeyboardButton(text='Youtube', callback_data='1')],
    #                                        [InlineKeyboardButton(text='Youtube', callback_data='1')],
    #                                       [[InlineKeyboardButton(text='Youtube', callback_data='1')]]
    #                                        ]),
    #
    # )
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text='some text',
    # )
    # inline_keyboard = [
    #     [InlineKeyboardButton(text='Кнопка 1', callback_data='button1'), InlineKeyboardButton(text='Кнопка 2', callback_data='button1')],
    #     [InlineKeyboardButton(text='Кнопка 3', callback_data='button1')],
    # ]
    # keyboard1 = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    builder = InlineKeyboardBuilder()
    for index in range(1, 11):
        builder.button(text=f"Set11111111111111 {index}", callback_data=f"set:{index}")
    builder.adjust(3, 2)
    await message.answer(text='some text', reply_markup=builder.as_markup())

@dp.callback_query()
async def answer(callback_query: CallbackQuery):
    message = callback_query.message
    data = callback_query.data.split(':')
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=message.message_id,
                                text=data[1],
                                reply_markup=message.reply_markup,
                                )