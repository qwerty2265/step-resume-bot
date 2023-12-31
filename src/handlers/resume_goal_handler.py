from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_goal_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 5</b>: Напишите свой номер телефона.
Укажите актуальный номер телефона, на который вы 100% ответите в рабочее время.
'''
    input_message = msg.text
    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1, keyboard_button2)

    if input_message.lower() == 'пропустить шаг':
        async with state.proxy() as data:
            data['goal'] = ''
        await ResumeFormState.next()
        with open('./public/images/5_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file, reply_markup=keyboard,caption=message)
    
    async with state.proxy() as data:
            if input_message.lower() != 'вернуться на прошлый шаг': data['goal'] = input_message
    await ResumeFormState.next()
    with open('./public/images/5_step.png', 'rb') as photo_file:
        return await msg.answer_photo(photo_file, reply_markup=keyboard,caption=message)