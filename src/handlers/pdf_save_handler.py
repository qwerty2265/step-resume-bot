from aiogram import types
from aiogram.dispatcher import FSMContext
from database.commands.sqlite_add_command import sqlite_add_command
from database.commands.sqlite_select_by_phone_command import sqlite_select_by_phone_command
from ..state import ResumeFormState

async def pdf_save_handler(msg: types.Message, state: FSMContext) -> None:
    await sqlite_add_command(state)
    async with state.proxy() as data:
        phone_number = data.get("phone_number")

    if phone_number:
        message: str = f'''
Минуту...
Номер телефона пользователя: {phone_number}
'''
    else:
        message: str = '''
Минуту...
Номер телефона пользователя не найден в памяти.
'''

    decrypted_data = sqlite_select_by_phone_command(phone_number)
    print(decrypted_data)

    keyboard_button = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button)

    return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")