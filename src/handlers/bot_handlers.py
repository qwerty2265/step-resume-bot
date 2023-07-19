from aiogram import types, filters
from .callcenter_handler import callcenter_handler
from .resume_fullname_handler import resume_fullname_handler
from .resume_city_handler import resume_city_handler
from ..state import *

def register_handlers(dp):
    dp.register_message_handler(
        callcenter_handler, state=UserState.ShowCallcenters, content_types=types.ContentTypes.TEXT
    )

    dp.register_message_handler(
        resume_fullname_handler, state=ResumeFormState.UserFullName, content_types=types.ContentTypes.TEXT
    )
    dp.register_message_handler(
        resume_city_handler, state=ResumeFormState.UserCity, content_types=types.ContentTypes.TEXT
    )

