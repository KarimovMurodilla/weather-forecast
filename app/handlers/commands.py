from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from loader import bot, pg
from app.config import ADMINS, GROUP_ID


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет {message.from_user.first_name}!")

    image = pg.put_all_info_on_photo()

    with open(image, 'rb') as img:
        await bot.send_photo(
            GROUP_ID, 
            img, 
            caption = "Дешевые авиабилеты, гостиницы и страховки"
                      " в Израиле 🇮🇱 <a href='https://t.me/theisraely/21'>Подробности здесь</a>"
        
        )
    

def register_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, chat_id=ADMINS, commands='start', state = '*')