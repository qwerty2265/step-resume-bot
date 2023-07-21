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

    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Вернуться в начало')
    keyboardFail = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboardFail.add(keyboard_button2)
    keyboardPass = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboardPass.add(keyboard_button1, keyboard_button2)

    if count_spaces_inside_string(input_message) < 1:
        error_message = 'Ваш ответ должен содержать как минимум 2 слова'
    
    if not contains_only_letters(input_message):
        error_message = 'Ваш ответ должен содержать только буквы.'

    if contains_only_letters(input_message) and count_spaces_inside_string(input_message) >= 1:
        async with state.proxy() as data:
            data["full_name"] = msg.text
        await ResumeFormState.next()

        with open('./public/images/2_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file, reply_markup=keyboardPass, caption=message)

    await msg.answer(error_message, reply_markup=keyboardFail, parse_mode="HTML")