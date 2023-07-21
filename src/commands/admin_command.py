from aiogram import types
from ..state import AdminState

async def admin_command(msg: types.Message) -> None:

    if msg.chat.type == "group":
        message: str = '''
Введите пароль
'''     
        await AdminState.AdminPassword.set()
        await msg.answer(message)
