from aiogram import types
from .start_command import start_command
from .callcenter_command import callcenter_command

def register_commands(dp):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(callcenter_command, commands=['callcenters'])
    dp.register_message_handler(callcenter_command, lambda message: message.text.lower() == 'контакты кц')