from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет {message.from_user.first_name}!")
    

def register_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start', state = '*')

