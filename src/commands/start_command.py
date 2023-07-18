from aiogram import types

async def start_command(msg: types.Message) -> None:
    message: str = 'Привет, студент!) Я создан для того, чтобы помогать в составление резюме. Я помогу тебе сделать первый шаг в увлекательный мир профессионального развития и карьерного продвижения.'

    keyboard_button1 = types.KeyboardButton(text='Хочу составить резюме')
    keyboard_button2 = types.KeyboardButton(text='Контакты КЦ')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(keyboard_button1)
    keyboard.add(keyboard_button2)

    await msg.answer(message, reply_markup=keyboard)