from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from loader import bot, owm
from app.config import GROUP_ID

from misc.photo_generator.generator import PhotoGenerator


pg = PhotoGenerator()


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет {message.from_user.first_name}!")
    

def register_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start', state = '*')