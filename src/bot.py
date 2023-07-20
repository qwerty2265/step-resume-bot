import os
from typing import Final
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, executor
from src.commands import bot_commands
from src.handlers import bot_handlers
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

load_dotenv();
BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
STORAGE = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=STORAGE)

def start_bot() -> None:
    logging.info('Starting...')
    bot_commands.register_commands(dp)
    bot_handlers.register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
    