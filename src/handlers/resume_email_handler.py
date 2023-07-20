from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
from ..utils import contains_at_symbol

async def resume_email_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 6</b>: Укажите свое образование. 

Если нет высшего образование можете указать дополнительное образования курсы, которые проходили и т.д.
'''
    input_message: str = msg.text
    error_message: str = 'Случилась непредвиденная ошибка.'

    if contains_at_symbol(input_message):
        async with state.proxy() as data:
            data["email"] = input_message
        
    if not contains_at_symbol(input_message) and input_message != 'Вернуться на прошлый шаг':
        error_message = 'Ваш ответ должен включать в себе "@".'
        return await msg.answer(error_message, parse_mode="HTML")

    await ResumeFormState.next();
    return await msg.answer(message, parse_mode="HTML")