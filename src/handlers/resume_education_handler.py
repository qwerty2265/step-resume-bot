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
    input_message = msg.text

    keyboard_button1 = types.KeyboardButton(text='Вернуться на прошлый шаг')
    keyboard_button2 = types.KeyboardButton(text='Вернуться в начало')
    keyboard_button3 = types.KeyboardButton(text='Нет опыта работы')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1, keyboard_button2)
    keyboard.add(keyboard_button3)

    async with state.proxy() as data:
        if input_message.lower() != 'вернуться на прошлый шаг': data['education'] = input_message
    await ResumeFormState.next()
    with open('./public/images/7_step.png', 'rb') as photo_file:
        return await msg.answer_photo(photo_file, reply_markup=keyboard,caption=message)