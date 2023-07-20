from database.encrypt_decrypt import decrypt_data
from aiogram.dispatcher import FSMContext
from database.sqlite_db import database, cursor

def sqlite_select_by_phone(phone_number):
    cursor.execute(
        'SELECT full_name, city, image, goal, phone_number, email, education, experience, hardskills, softskills, add_info FROM users WHERE phone_number = ?',
        (phone_number)
    )
    result = cursor.fetchone()

    if result:
        decrypted_data = decrypt_data(result)
        return decrypted_data
