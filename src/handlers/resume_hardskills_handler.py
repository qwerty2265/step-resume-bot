from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_hardskills_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 9: Навыки Soft skills

Коммуникабельность, ответственность, уверенный пользователь ПК…
Если ваш опыт не доказывает всех этих качеств – не пишите.

Лучше указывайте soft skills. Например:
- Навык ведения тренингов.
- Навык управления несколькими проектами.
- Высокий эмоциональный интеллект.
- Знание иностранного языка и т.п.

А если вам хочется рассказать о своих личных качествах, то упомяните их в разделе «Дополнительные сведения».
'''

    await ResumeFormState.next();
    await msg.answer(message)