from src import bot
from database import sqlite_db

if __name__ == "__main__":
    try:
        sqlite_db.sqlite_start()
        bot.start_bot()
    except Exception as ex:
        print(ex)