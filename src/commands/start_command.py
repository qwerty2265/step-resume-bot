import os
from aiogram import types
from aiogram.dispatcher import FSMContext

async def start_command(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Привет, студент!) Я создан для того, чтобы помогать в составление резюме.
Я помогу тебе сделать первый шаг в увлекательный мир профессионального развития и карьерного продвижения

Для более подробной информации напиши /help
'''
    await state.finish()
    
    keyboard_button1 = types.KeyboardButton(text='Хочу составить резюме')
    keyboard_button2 = types.KeyboardButton(text='Контакты КЦ')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(keyboard_button1)
    keyboard.add(keyboard_button2)

    with open('./public/images/logo.png', 'rb') as photo_file:
        await msg.answer_photo(photo_file, caption=message, reply_markup=keyboard)
