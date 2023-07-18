from aiogram import types, filters
from .callcenter_handler import callcenter_handler

def register_handlers(dp):
    dp.register_message_handler(callcenter_handler, lambda msg: msg.text == 'Контакты КЦ')