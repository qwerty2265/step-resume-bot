from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_experience_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 8: Подробно распишите ваши профессиональные навыки.
Золотое правило составление резюме:

Указывайте только то, что относиться к требованиям вакансии. Укажите только практические навыки. 
Например, владение конкретными языками программирования, поддержка и администрирование серверного оборудования или владение специализированными программами.  
'''

    await ResumeFormState.next();
    await msg.answer(message)