from aiogram import types
from .start_command import start_command

def register_handlers(dp):
    dp.register_message_handler(start_command, commands=['start'])