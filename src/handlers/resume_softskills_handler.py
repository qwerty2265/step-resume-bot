from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_softskills_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 10</b>: Дополнительные сведения.

Пример, как правильно заполнять этот раздел:
Верно:
Выстраиваю отношения с коллегами и клиентами, основанные на взаимоуважение и доверии.

Неверно:
Коммуникабельность.
'''
    input_message = msg.text

    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Завершить')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1,keyboard_button2)

    async with state.proxy() as data:
            if input_message.lower() != 'вернуться на прошлый шаг': data['softskills'] = input_message
    await ResumeFormState.next()
    with open('./public/images/10_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file, reply_markup=keyboard,caption=message)