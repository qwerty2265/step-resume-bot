from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState

async def resume_image_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Шаг 4: Укажите цель поиска.

Это опциональный блок, его не всегда нужно заполнять – все зависит от ваших навыков и вакансии.

Если пишите желаемую зарплату, возьмите средний размер оплаты из реальных предложений и прибавьте 10%.

Исследуйте самостоятельно рынок. Оцените свой опыт работы и посмотрите, в какой ценовой промежуток по зарплате попадаете.
Так вы сможете узнать, сколько стоит ваша работа, и рассказать ожидания на собеседовании.
'''
    error_message: str = 'Ваше сообщение должно содержать только фотографию.'
    
    if msg.photo:
        await ResumeFormState.next();
        await msg.answer(message)
        return
    

    await msg.answer(error_message)