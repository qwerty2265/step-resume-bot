from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import ResumeFormState
from ..commands.resume_command import resume_command
from .resume_fullname_handler import resume_fullname_handler
from .resume_city_handler import resume_city_handler
from .resume_image_handler import resume_image_handler
from .resume_goal_handler import resume_goal_handler
from .resume_phonenumber_handler import resume_phonenumber_handler
from .resume_email_handler import resume_email_handler
from .resume_education_handler import resume_education_handler
from .resume_experience_handler import resume_experience_handler
from .resume_hardskills_handler import resume_hardskills_handler
from .resume_softskills_handler import resume_softskills_handler

async def come_back_handler(msg: types.Message, state: FSMContext) -> None:
    await ResumeFormState.previous()
    state_now = await state.get_state()
    state_now = state_now.replace(':', '.')

    match state_now:
        case 'ResumeFormState.UserFullName':
            return await resume_command(msg)

        case 'ResumeFormState.UserCity':
            await ResumeFormState.previous()
            return await resume_fullname_handler(msg, state)

        case 'ResumeFormState.UserImage':
            await ResumeFormState.previous()
            return await resume_city_handler(msg, state)

        case 'ResumeFormState.UserGoal':
            await ResumeFormState.previous()
            return await resume_image_handler(msg, state)

        case 'ResumeFormState.UserPhoneNumber':
            await ResumeFormState.previous()
            return await resume_goal_handler(msg, state)

        case 'ResumeFormState.UserEmail':
            await ResumeFormState.previous()
            return await resume_phonenumber_handler(msg, state)

        case 'ResumeFormState.UserEducation':
            await ResumeFormState.previous()
            return await resume_email_handler(msg, state)

        case 'ResumeFormState.UserExperience':
            await ResumeFormState.previous()
            return await resume_education_handler(msg, state)

        case 'ResumeFormState.UserHardSkills':
            await ResumeFormState.previous()
            return await resume_experience_handler(msg, state)

        case 'ResumeFormState.UserSoftSkills':
            await ResumeFormState.previous()
            return await resume_hardskills_handler(msg, state)

        case 'ResumeFormState.UserAdditionalInformation':
            await ResumeFormState.previous()
            return await resume_softskills_handler(msg, state)