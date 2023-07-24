from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_hardskills_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 9</b>: Навыки Soft skills

Коммуникабельность, ответственность, уверенный пользователь ПК…
Если ваш опыт не доказывает всех этих качеств – не пишите.

Лучше указывайте soft skills. Например:
•	Навык ведения тренингов.
•	Навык управления несколькими проектами.
•	Высокий эмоциональный интеллект.
•	Знание иностранного языка и т.п.

А если вам хочется рассказать о своих личных качествах, то упомяните их в разделе «Дополнительные сведения».
'''
    input_message = msg.text

    async with state.proxy() as data:
            if input_message.lower() != 'вернуться на прошлый шаг': data['hardskills'] = input_message
    await ResumeFormState.next()
    with open('./public/images/9_step.png', 'rb') as photo_file:
            return await msg.answer_photo(photo_file,caption=message)