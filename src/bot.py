import os
from typing import Final
from dotenv import load_dotenv
from aiogram import types, Dispatcher, Bot, executor

load_dotenv();
BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
BOT_USERNAME: Final = os.getenv('BOT_USERNAME')

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

def start_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True)