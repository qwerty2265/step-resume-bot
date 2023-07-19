from aiogram import types, filters
from .callcenter_handler import callcenter_handler
from .resume_handler import resume_handler
from ..state import *

def register_handlers(dp):
    dp.register_message_handler(
        callcenter_handler, state=UserState.ShowCallcenters, content_types=types.ContentTypes.TEXT
    )

    dp.register_message_handler(
        resume_handler, state=UserState.CreateResume, content_types=types.ContentTypes.TEXT
    )