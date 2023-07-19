from aiogram import types
from ..state import ResumeFormState, UserState

async def resume_command(msg: types.Message) -> None:
    message: str = '''
<b>Шаг 1</b>: Напиши свое ФИО.
Желательно напиши свое ФИО так, как написано у тебя в государственных документах (удостоверение личности).
'''

    keyboard_button = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button)


    await ResumeFormState.UserFullName.set()
    await msg.answer(message, reply_markup=keyboard)
