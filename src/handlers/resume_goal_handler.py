from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_goal_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 5</b>: Напишите свой номер телефона.
Укажите актуальный номер телефона, на который вы 100% ответите в рабочее время.
'''
    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1, keyboard_button2)

    if msg.text.lower() == 'пропустить шаг':
        async with state.proxy() as data:
            data["goal"] = ''
        await ResumeFormState.next();
        return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")
    
    async with state.proxy() as data:
            data["goal"] = msg.text
    await ResumeFormState.next();
    return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")