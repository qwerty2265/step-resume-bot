from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
from ..utils import contains_only_letters

async def resume_fullname_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 2: Напиши свой город, в котором вы ищете работу.
'''
    input_message: str = msg.text
    error_message: str = 'Ваш ответ должен содержать только буквы.'

    if contains_only_letters(input_message):
        await ResumeFormState.next();
        await msg.answer(message)
        return

    await msg.answer(error_message)