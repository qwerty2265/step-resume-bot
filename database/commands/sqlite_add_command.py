from database.encrypt_decrypt import encrypt_data
from aiogram.dispatcher import FSMContext
from database.sqlite_db import database, cursor

async def sqlite_add_command(state: FSMContext) -> None:
    async with state.proxy() as data:
        encrypted_data = encrypt_data(data)
        encrypted_data_tuple = tuple(encrypted_data)

        cursor.execute(
            'INSERT INTO users (full_name, city, image, goal, phone_number, email, education, experience, hardskills, softskills, add_info) VALUES (?,?,?,?,?,?,?,?,?,?,?)', encrypted_data_tuple
        )
        database.commit()