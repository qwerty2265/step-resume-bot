from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_softskills_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 10: Дополнительные сведения.

Пример, как правильно заполнять этот раздел:
Верно:
Выстраиваю отношения с коллегами и клиентами, основанные на взаимоуважение и доверии.
Неверно:
Коммуникабельность.
'''

    await ResumeFormState.next();
    await msg.answer(message)