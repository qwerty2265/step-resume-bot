from aiogram import types
from aiogram.dispatcher.filters import Text
from .start_command import start_command
from .callcenter_command import callcenter_command
from .resume_command import resume_command
from .help_command import help_command
from ..state import *

def register_commands(dp):
    dp.register_message_handler(start_command, commands=['start'], state="*")
    dp.register_message_handler(
        start_command, Text(equals="вернуться в начало", ignore_case=True), state="*"
    )

    dp.register_message_handler(help_command, commands=['help'], state="*")

    dp.register_message_handler(callcenter_command, commands=['callcenters'], state="*")
    dp.register_message_handler(
        callcenter_command, Text(equals='контакты кц', ignore_case=True)
    )

    dp.register_message_handler(
        callcenter_command, Text(equals='вернуться к выбору филиала', ignore_case=True) , state=CallCenterState.CallCenterCity
    )

    dp.register_message_handler(resume_command, commands=['resume'], state="*")
    dp.register_message_handler(
        resume_command, Text(equals='хочу составить резюме', ignore_case=True)
    )
