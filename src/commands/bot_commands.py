from aiogram import types
from .start_command import start_command
from .callcenter_command import callcenter_command
from .resume_command import resume_command
from ..state import *

def register_commands(dp):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(
        start_command, lambda message: message.text.lower() == "вернуться в начало", state=CallCenterState.CallCenterCity
    )
    dp.register_message_handler(
        start_command, lambda message: message.text.lower() == "вернуться в начало", state=UserState.CreateResume
    )

    dp.register_message_handler(callcenter_command, commands=['callcenters'], state=None)
    dp.register_message_handler(
        callcenter_command, lambda message: message.text.lower() == 'контакты кц', state=None
    )
    dp.register_message_handler(
        callcenter_command, lambda message: message.text.lower() == 'вернуться к выбору филиала', state=CallCenterState.CallCenterCity
    )

    dp.register_message_handler(resume_command, commands=['resume'], state=None)
    dp.register_message_handler(
        resume_command, lambda message: message.text.lower() == 'хочу составить резюме', state=None
    )
