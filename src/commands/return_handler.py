from aiogram import types
from aiogram.dispatcher import FSMContext

async def return_handler(msg: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await msg.reply("OK")