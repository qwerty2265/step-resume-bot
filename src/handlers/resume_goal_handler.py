from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_goal_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 5</b>: Напишите свой номер телефона.
Укажите актуальный номер телефона, на который вы 100% ответите в рабочее время.
'''

    async with state.proxy() as data:
            data["goal"] = msg.text
    await ResumeFormState.next();
    return await msg.answer(message, parse_mode="HTML")