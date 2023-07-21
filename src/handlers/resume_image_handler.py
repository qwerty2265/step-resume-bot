import os
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from ..state import ResumeFormState


async def resume_image_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
<b>Шаг 4</b>: Укажите цель поиска.

Это опциональный блок, его не всегда нужно заполнять – все зависит от ваших навыков и вакансии.

Если пишите желаемую зарплату, возьмите средний размер оплаты из реальных предложений и прибавьте 10%.

Исследуйте самостоятельно рынок. Оцените свой опыт работы и посмотрите, в какой ценовой промежуток по зарплате попадаете.
Так вы сможете узнать, сколько стоит ваша работа, и рассказать ожидания на собеседовании.
'''
    error_message: str = 'Ваше сообщение должно содержать только фотографию.'
    
    if msg.photo:
        # Конвертация изображения в биты
        load_dotenv()
        BOT_TOKEN = os.getenv('BOT_TOKEN')
        bot = Bot(BOT_TOKEN) 
        image = msg.photo
        image_info = await bot.get_file(image[len(image) - 1].file_id)
        new_image = (await bot.download_file(image_info.file_path)).read()
        await bot.close()

        async with state.proxy() as data:
            data["image"] = new_image
        await ResumeFormState.next();
        return await msg.answer(message,parse_mode="HTML")
    
    elif msg.text.lower() == 'пропустить шаг':
        async with state.proxy() as data:
            data["image"] = ''
        await ResumeFormState.next();
        return await msg.answer(message, parse_mode="HTML")

    
    await msg.answer(error_message, parse_mode="HTML")
