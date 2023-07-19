from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
from ..utils import contains_only_letters, count_spaces_inside_string

async def resume_fullname_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 2</b>: Напиши свой город, в котором вы ищете работу.
'''
    input_message: str = msg.text
    error_message: str = 'Случилась непредвиденная ошибка.'

    if count_spaces_inside_string(input_message) < 1:
        error_message = 'Ваш ответ должен содержать как минимум 2 слова'
    
    if not contains_only_letters(input_message):
        error_message = 'Ваш ответ должен содержать только буквы.'

    if contains_only_letters(input_message) and count_spaces_inside_string(input_message) >= 1:
        await ResumeFormState.next();
        await msg.answer(message, parse_mode="HTML")
        return

    await msg.answer(error_message, parse_mode="HTML")