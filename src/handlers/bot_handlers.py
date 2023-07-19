from aiogram import types, filters
from .callcenter_handler import callcenter_handler
from .resume_fullname_handler import resume_fullname_handler
from .resume_city_handler import resume_city_handler
from .resume_image_handler import resume_image_handler
from .resume_goal_handler import resume_goal_handler
from .resume_phonenumber_handler import resume_phonenumber_handler
from .resume_email_handler import resume_email_handler
from .resume_education_handler import resume_education_handler
from .resume_hardskills_handler import resume_hardskills_handler
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
    dp.register_message_handler(
        resume_image_handler, state=ResumeFormState.UserImage, content_types=types.ContentTypes.PHOTO
    )
    dp.register_message_handler(
        resume_goal_handler, state=ResumeFormState.UserGoal, content_types=types.ContentTypes.TEXT
    )
    dp.register_message_handler(
        resume_phonenumber_handler, state=ResumeFormState.UserPhoneNumber, content_types=types.ContentTypes.TEXT
    )
    dp.register_message_handler(
        resume_email_handler, state=ResumeFormState.UserEmail, content_types=types.ContentTypes.TEXT
    )
    dp.register_message_handler(
        resume_education_handler, state=ResumeFormState.UserEducation, content_types=types.ContentTypes.TEXT
    )
    dp.register_message_handler(
        resume_hardskills_handler, state=ResumeFormState.UserHardSkills, content_types=types.ContentTypes.TEXT
    )
