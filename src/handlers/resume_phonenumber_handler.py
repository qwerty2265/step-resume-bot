from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
from ..utils import contains_phone_number

async def resume_phonenumber_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 5.1: Укажите адрес электронный адрес почты.

Идеальный вариант – это словосочетание фамилии с именем. 
Если такой нет – заведите специально для рабочих контактов. 
Почта кошечка92 и прочие проявления фантазии рекрутеры не воспринимают всерьез.
'''
    input_message: str = msg.text
    error_message: str = 'Ваш ответ должен содержать только цифры и знак "+".'

    if contains_phone_number(input_message):
        await ResumeFormState.next();
        await msg.answer(message)
        return

    await msg.answer(error_message)