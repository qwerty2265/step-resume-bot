from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def pdf_save_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Минуту...
'''

    keyboard_button1 = types.KeyboardButton(text='Сохранить в pdf')
    keyboard_button2 = types.KeyboardButton(text='Сохранить в docx')
    keyboard_button3 = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1, keyboard_button2)
    keyboard.add(keyboard_button3)

    return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")