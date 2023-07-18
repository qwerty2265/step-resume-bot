from aiogram import types

async def start_command(msg: types.Message) -> None:
    await msg.answer('Привет, студент!) Я создан для того, чтобы помогать в составление резюме. Я помогу тебе сделать первый шаг в увлекательный мир профессионального развития и карьерного продвижения. ')