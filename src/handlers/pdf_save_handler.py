import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from database.commands.sqlite_add_command import sqlite_add_command
from database.commands.sqlite_select_by_phone_command import sqlite_select_by_phone_command
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import logging

async def pdf_save_handler(msg: types.Message, state: FSMContext) -> None:
    # Заносит данные в базу данных
    await sqlite_add_command(state)
    # Вытаскивает номер телефона для поиска по нему
    async with state.proxy() as data:
        phone_number = data.get('phone_number')

    if phone_number:
        message: str = f'''
Это может занять некоторое время...
'''
    else:
        message: str = '''
Это может занять некоторое время...

Пользователь не найден в памяти.
Попробуйте заполнить таблицу еще раз.
'''

    error_message: str = '''
Случилась непредвиденная ошибка
'''
    keyboard_button = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button)
    
    # Зашифрованные данные пользователя
    try:
        decrypted_data = sqlite_select_by_phone_command(phone_number)
    except Exception as ex:
        logging.error('Пользователь не был найден')
        logging.error(ex)
        return await msg.answer(error_message, reply_markup=keyboard, parse_mode='HTML')

    # Создание пдф документа
    try:
        pdf_file = generate_pdf(decrypted_data)

        if os.path.exists(pdf_file):
            with open(pdf_file, 'rb') as file:
                await msg.answer(message, reply_markup=keyboard, parse_mode='HTML')
                await msg.answer_document(file, reply_markup=keyboard)
                os.remove(pdf_file)
                await state.finish()
                return
    except Exception as ex:
        logging.error('Не удалось создать пфд документ')
        logging.error(ex)
        return await msg.answer(error_message, reply_markup=keyboard, parse_mode='HTML')



def generate_pdf(data):
    pdf_file = 'resume.pdf'
    c = canvas.Canvas(pdf_file, pagesize=letter)

    script_path = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_path, '../../public/fonts/FreeSans.ttf')
    pdfmetrics.registerFont(TTFont('FreeSans', font_path))
    c.setFont('FreeSans', size=15)
    top_margin = 100
    y = 800 - top_margin

    for value in data:
        
        if isinstance(value, bytes):
            with open('temp_image.jpg', 'wb') as f:
                f.write(value)
            image = Image.open('temp_image.jpg')

            img_width, img_height = image.size
            aspect_ratio = img_width / img_height
            if img_width > img_height:
                box_width = 100
                box_height = int(100 / aspect_ratio)
            else:
                box_width = int(100 * aspect_ratio)
                box_height = 100

            c.drawImage('temp_image.jpg', 400, y, width=box_width, height=box_height)

            y -= box_height + 10

            image.close()
            os.remove('temp_image.jpg')
            continue

        if value != '':
            line = f'- {value}'
            c.drawString(72, y, line, mode=0)
            y -= 30

    c.save()
    return pdf_file
