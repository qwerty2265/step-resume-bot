from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
import logging 

async def resume_additionalinformation_handler(msg: types.Message, state: FSMContext) -> None:
    message: str = '''
Спасибо за использование бота для составления вашего резюме!

Резюме будет на рассмотрении у HR.
А также будет выслано вам в виде pdf/docx файла.
'''
    input_message = msg.text

    keyboard_button1 = types.KeyboardButton(text='Сохранить в pdf')
    keyboard_button2 = types.KeyboardButton(text='Сохранить в docx (не работает)')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button1)
    keyboard.add(keyboard_button2)

    if input_message.lower() != 'вернуться на прошлый шаг':
        async with state.proxy() as data:
            if input_message =='Завершить':
                input_message = ''
                
            data['add_info'] = input_message
        
        await ResumeFormState.next()
        return await msg.answer(message, reply_markup=keyboard, parse_mode='HTML')