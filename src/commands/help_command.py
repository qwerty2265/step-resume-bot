from aiogram import types
from aiogram.dispatcher import FSMContext

async def help_command(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Привет, студент!) Я создан для того, чтобы помогать в составление резюме.
Я помогу тебе сделать первый шаг в увлекательный мир профессионального развития и карьерного продвижения.

Для этого у меня есть:

/resume - команда, для начала составления резюме.

/callcenters - команда, показывающая список доступных колл-центров
'''

    keyboard_button = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button)

    await state.finish()
    await msg.answer(message, reply_markup=keyboard)
