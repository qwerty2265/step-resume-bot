from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_email_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 6: Укажите свое образование. 

Если нет высшего образование можете указать дополнительное образования курсы, которые проходили и т.д.
'''

    await ResumeFormState.next();
    await msg.answer(message)