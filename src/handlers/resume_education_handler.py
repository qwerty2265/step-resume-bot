from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_education_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 7</b>: Напишите про свой опыт работы.

Конкретизируйте. Рекрутеров интересуют цифры и факты, поэтому 
«Значительно повысил посещаемость сайта» заменяйте на «Повысил посещаемость на 12% за квартал».

<b>Внимание!</b>
Не стоит врать о своем резюме или приукрашивать. 
Помните, если на собеседовании вам все-таки удастся убедить работодателя или заказчика, что вы подходите, то уже в процессе работы обман 100% будет раскрыт.
'''

    await ResumeFormState.next();
    await msg.answer(message, parse_mode="HTML")