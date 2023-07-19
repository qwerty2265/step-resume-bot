from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_fullname_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 2: Напиши свой город, в котором вы ищете работу.
'''
    input_message: str = msg.text
    error_message: str = 'Ваш ответ должен содержать только буквы.'

    def contains_only_letters(string: str) -> bool:
        input_string = ''.join(string.split())
        return input_string.isalpha()

    if contains_only_letters(input_message):
        await ResumeFormState.UserCity.set();
        await msg.answer(message)
        return

    
    await msg.answer(error_message)