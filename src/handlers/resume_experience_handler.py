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
    no_ex_message: str = '''
Отлично, ты перешел в раздел нет опыта работы. Ты задаешься вопросам что писать, когда опыта работы нет?
Запомни! 
Любой опыт – это опыт, не забывайте его указывать.
Есть разные возможности получить первичный опты. И в резюме вносим его именно в графу «место работы», например:
•	Опыт в профильных соревнованиях во время обучения.
•	Опыт создания проектов для семьи/друзей.
•	Опыт стажировки.
•	Волонтерство.
•	Собственный проект.
'''
    step_7_message: str = '''
<b>Шаг 7</b>: Напишите про свой опыт работы.

Конкретизируйте. Рекрутеров интересуют цифры и факты, поэтому 
«Значительно повысил посещаемость сайта» заменяйте на «Повысил посещаемость на 12% за квартал».
'''

    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1, keyboard_button2)

    if msg.text.lower() == 'нет опыта работы':
        await msg.answer(no_ex_message, parse_mode="HTML")
        with open('./public/images/7_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file, caption=step_7_message)

    else:
        async with state.proxy() as data:
                data["experience"] = msg.text
        await ResumeFormState.next();
        with open('./public/images/8_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file, reply_markup=keyboard, caption=message)