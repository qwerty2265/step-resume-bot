from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
from ..utils import contains_only_letters

async def resume_city_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 3</b>: Загрузите свое фото.

Фото – та деталь, с которой HR начнет знакомство с вами. 
Не размещайте в своем резюме селфи, мелкие и некачественные фотографии, фото в компании других людей или с общего застолья. 
Рекомендации:

•	Остановите выбор на портретном фото или фото в деловом стиле;
•	Выберите нейтральный фон;
•	Обратите внимание на качество фотографии;
•	И не забывайте про улыбку – она притягивает внимание и распологает.

'''
    input_message: str = msg.text
    error_message: str = 'Ваш ответ должен содержать только буквы.'

    if contains_only_letters(input_message):
        await ResumeFormState.next()
        await msg.answer(message, parse_mode="HTML")
        return

    await msg.answer(error_message, parse_mode="HTML")