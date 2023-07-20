from aiogram import types
from aiogram.dispatcher import FSMContext
from database.commands import sqlite_add_command
from ..state import ResumeFormState

async def resume_additionalinformation_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Спасибо за использование бота для составления вашего резюме!

Резюме будет на рассмотрении у HR.
А также будет выслано вам в виде pdf/docx файла.
'''

    keyboard_button1 = types.KeyboardButton(text='Сохранить в pdf')
    keyboard_button2 = types.KeyboardButton(text='Сохранить в docx')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1)
    keyboard.add(keyboard_button2)

    try:
        async with state.proxy() as data:
            data["add_info"] = msg.text
        await sqlite_add_command.sqlite_add_command(state)
    except Exception as ex:
        print(ex)
    await ResumeFormState.next()
    return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")