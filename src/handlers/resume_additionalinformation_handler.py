from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_additionalinformation_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Спасибо за использование бота для составления вашего резюме!

Резюме будет на рассмотрении у HR.
А также будет выслано вам в виде pdf файла.
'''

    keyboard_button1 = types.KeyboardButton(text='Вернуться в начало')
    keyboard_button2 = types.KeyboardButton(text='Завершить')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1)
    keyboard.add(keyboard_button2)

    await ResumeFormState.finish();
    await msg.answer(message, reply_markup=keyboard)