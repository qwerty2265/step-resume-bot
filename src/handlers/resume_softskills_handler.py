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
    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Завершить')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1,keyboard_button2)

    async with state.proxy() as data:
            data["softskills"] = msg.text
    await ResumeFormState.next();
    return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")