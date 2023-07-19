from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
from ..state import UserState

async def resume_command(msg: types.Message) -> None:
    message: str = '''
Шаг 1: Напиши свое ФИО.
Желательно напиши свое ФИО так как в написано у тебя в государственных документах (удостоверение личности).
'''

    keyboard_button1 = types.KeyboardButton(text='Вернуться в начало')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(keyboard_button1)

    await msg.answer(message, reply_markup=keyboard)