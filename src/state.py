from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    Start = State()
    CreateResume = State()
    ShowCallcenters = State()

class CallCenterState(StatesGroup):
    CallCenterCity = State()
    
class ResumeFormState(StatesGroup):
    UserFullName = State()
    UserCity = State()
    UserImage = State()
    UserGoal = State()
    UserPhoneNumber = State()
    UserEmail = State()
    UserEducation = State()
    UserExperience = State()
    UserHardSkills = State()
    UserSoftSkills = State()
    UserAdditionalInformation = State()

class ResumeSkipState(StatesGroup):
    SkipStep = State()