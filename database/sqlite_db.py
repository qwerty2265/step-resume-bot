import sqlite3 as sqlite
from typing import Final
from .key_generate import key_generate
import logging

def sqlite_start():
    global database, cursor
    path: Final = './database/telegram_bot_users_resume.db'
    database = sqlite.connect(path)
    cursor = database.cursor()

    if not database:
        logging.error('DATABASE IS NOT CONNECTED')
        return
    
    logging.info('Connected...')
    key_generate()

    database.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        city TEXT NOT NULL,
        image BLOB NOT NULL,
        goal TEXT,
        phone_number TEXT NOT NULL,
        email TEXT NOT NULL,
        education TEXT NOT NULL,
        experience TEXT NOT NULL,
        hardskills TEXT NOT NULL,
        softskills TEXT NOT NULL,
        add_info TEXT
    )
    ''')
    database.commit()

    