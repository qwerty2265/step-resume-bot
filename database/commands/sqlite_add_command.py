from ..sqlite_db import cursor, database
from ..encrypt_decrypt import encrypt_data

async def sqlite_add_command(state) -> None:
    async with state.proxy() as data:
        encrypted_data = encrypt_data(','.join(data.values()))
        cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?,?)', tuple(encrypted_data))
        database.commit()