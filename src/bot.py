import os
from typing import Final
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, executor
from .commands import bot_commands
from .handlers import bot_handlers

load_dotenv();
BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

def start_bot() -> None:
    print('Starting...')
    bot_handlers.register_handlers(dp)
    bot_commands.register_commands(dp)
    print('Polling...')
    executor.start_polling(dp, skip_updates=True)
    