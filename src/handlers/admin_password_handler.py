import os
from dotenv import load_dotenv
from aiogram import types
from aiogram.dispatcher import FSMContext
from ..state import AdminState

async def admin_password_handler(msg: types.Message, state: FSMContext) -> None:
    load_dotenv()
    admin_password = os.getenv('ADMIN_PASSWORD')
    
    if msg.text == admin_password:
        await AdminState.AdminStart.set()
        await msg.answer('Вы вошли как админ')