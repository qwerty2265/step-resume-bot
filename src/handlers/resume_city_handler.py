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
    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Вернуться в начало')
    keyboard_button3 = types.KeyboardButton(text='Пропустить шаг')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1, keyboard_button2)
    keyboard.add(keyboard_button3)

    if contains_only_letters(input_message):
        async with state.proxy() as data:
            data['city'] = msg.text
        await ResumeFormState.next()
        with open('./public/images/3_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file, caption=message, reply_markup=keyboard)

    await msg.answer(error_message, reply_markup=keyboard, parse_mode='HTML')