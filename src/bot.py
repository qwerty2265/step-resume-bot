import os
from typing import Final
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, executor
from .commands import bot_commands
from .handlers import bot_handlers
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv();
BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
STORAGE = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=STORAGE)

def start_bot() -> None:
    print('Starting...')
    bot_commands.register_commands(dp)
    bot_handlers.register_handlers(dp)
    print('Polling...')
    executor.start_polling(dp, skip_updates=True)
    