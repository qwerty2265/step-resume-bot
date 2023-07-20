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

    def generate_pdf(data):
        pdf_flie = "resume.pdf"
        print('enter')
        c = canvas.Canvas(pdf_flie, pagesize=letter)

        y = 800

        for value in data:
            # Форматируем строку с ключом и значением
            line = f"- {value}"

            # Вставляем строку на указанную высоту в PDF
            c.drawString(72, y, line)

            # Уменьшаем высоту для следующей строки данных
            y -= 20

        c.save()
        return pdf_flie

    decrypted_data = sqlite_select_by_phone_command(phone_number)
    print(decrypted_data)

     # Generate the PDF and get the file name
    pdf_file = generate_pdf(decrypted_data)

    # Check if the file exists before sending
    if os.path.exists(pdf_file):
        # Send the PDF file
        with open(pdf_file, "rb") as file:
            await msg.answer_document(file)

        # Remove the PDF file after sending
        os.remove(pdf_file)

    
    keyboard_button = types.KeyboardButton(text='Вернуться в начало')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(keyboard_button)

    return await msg.answer(message, reply_markup=keyboard, parse_mode="HTML")


