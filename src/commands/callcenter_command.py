from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup

async def callcenter_command(msg: types.Message) -> None:
    message: str = 'Контакты карьерного центра здесь вы можете обратиться в нужный карьерный центр.\nДля начала выберите филиал?'

    keyboard_button1 = types.KeyboardButton(text='Алматы')
    keyboard_button2 = types.KeyboardButton(text='Астана')
    keyboard_button3 = types.KeyboardButton(text='Караганда')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(keyboard_button1, keyboard_button2)
    keyboard.add(keyboard_button3)
    await msg.answer(message, reply_markup=keyboard)

