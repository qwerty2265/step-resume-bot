from aiogram import types
from aiogram.dispatcher import FSMContext
from database.encrypt_decrypt import encrypt_string
from ..state import ResumeFormState
from ..utils import contains_phone_number, correct_length_phone_number

async def resume_phonenumber_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 5.1</b>: Укажите адрес электронный адрес почты.

Идеальный вариант – это словосочетание фамилии с именем. 

Если такой нет – заведите специально для рабочих контактов. 

Почта кошечка92 и прочие проявления фантазии рекрутеры не воспринимают всерьез.
'''
    input_message: str = msg.text
    error_message: str = 'Случилась непредвиденная ошибка.'
    
    if contains_phone_number(input_message) and correct_length_phone_number(input_message):
        async with state.proxy() as data:
            if input_message.lower() != 'вернуться на прошлый шаг': data['phone_number'] = encrypt_string(input_message)
    
    elif not correct_length_phone_number(input_message) and input_message != 'Вернуться на прошлый шаг':
        error_message = 'Ваш ответ должен содержать минимум 11 символов.'
        return await msg.answer(error_message, parse_mode='HTML')

    elif not contains_phone_number(input_message) and input_message != 'Вернуться на прошлый шаг':
        error_message = 'Ваш ответ должен содержать только цифры и знак '+'.'
        return await msg.answer(error_message, parse_mode='HTML')

    await ResumeFormState.next()
    with open('./public/images/5.1_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file,caption=message)
    