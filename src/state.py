from aiogram.dispatcher.filters.state import State, StatesGroup

# Состояние пользователя в чате
class UserState(StatesGroup):
    Start = State()
    CreateResume = State()
    ShowCallcenters = State()

# Состояние команды /callcenters
class CallCenterState(StatesGroup):
    CallCenterCity = State()
    
# Состояние команды /resume
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