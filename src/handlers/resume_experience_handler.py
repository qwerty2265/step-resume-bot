from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_experience_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 8</b>: Подробно распишите ваши профессиональные навыки.
Золотое правило составление резюме:

•	Указывайте только то, что относиться к требованиям вакансии. Укажите только практические навыки. 
•	Например, владение конкретными языками программирования, поддержка и администрирование серверного оборудования или владение специализированными программами.  
'''
    async with state.proxy() as data:
            data["experience"] = msg.text
    await ResumeFormState.next();
    return await msg.answer(message, parse_mode="HTML")