from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_goal_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 5: Напишите свой номер телефона.
Укажите актуальный номер телефона, на который вы 100% ответите в рабочее время.
'''

    await ResumeFormState.next();
    await msg.answer(message)