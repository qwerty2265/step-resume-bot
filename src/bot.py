import os
from typing import Final
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, executor
from .commands import command_handler

load_dotenv();
BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

def start_bot() -> None:
    print('Polling...')
    command_handler.register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
    