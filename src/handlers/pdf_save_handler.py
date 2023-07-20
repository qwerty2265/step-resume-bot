import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from database.commands.sqlite_add_command import sqlite_add_command
from database.commands.sqlite_select_by_phone_command import sqlite_select_by_phone_command
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

async def pdf_save_handler(msg: types.Message, state: FSMContext) -> None:
    await sqlite_add_command(state)
    async with state.proxy() as data:
        phone_number = data.get("phone_number")

    if phone_number:
        message: str = f'''
Минуту...
'''
    else:
        message: str = '''
Минуту...
Пользователь не найден в памяти.
Попробуйте заполнить таблицу еще раз.
'''

    decrypted_data = sqlite_select_by_phone_command(phone_number)
    print(decrypted_data)

    pdf_file = generate_pdf(decrypted_data)

    if os.path.exists(pdf_file):
        with open(pdf_file, "rb") as file:
            await msg.answer_document(file)

        os.remove(pdf_file)

    
    keyboard_button = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button)

    return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")


def generate_pdf(data):
    pdf_file = "resume.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    top_margin = 100
    y = 800 - top_margin

    for value in data:
        line = f"- {value}"
        c.drawString(72, y, line)

        if isinstance(value, bytes):
            image_file = "temp_image.jpg"
            with open(image_file, "wb") as f:
                f.write(value)
            c.drawImage(image_file, 400, y, width=100, height=100)
            os.remove(image_file)

        y -= 20

    c.save()
    return pdf_file
