from database.encrypt_decrypt import encrypt_string, decrypt_list
from aiogram.dispatcher import FSMContext
from database.sqlite_db import database, cursor

def sqlite_select_by_phone_command(phone_number):
    cursor.execute(
        'SELECT full_name, city, image, goal, phone_number, email, education, experience, hardskills, softskills, add_info FROM users WHERE phone_number = ?',
        (phone_number, )
    )
    result = cursor.fetchone()

    if result:
        result_list = list(result)
        decrypted_data = decrypt_list(result_list)
        return decrypted_data
