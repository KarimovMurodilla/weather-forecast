from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from loader import bot
from app.config import GROUP_ID

from misc.photo_generator.generator import PhotoGenerator


pg = PhotoGenerator()


async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет {message.from_user.first_name}!")

    image = await pg.put_all_info_on_photo()

    with open(image, 'rb') as img:
        await bot.send_photo(
            message.chat.id, 
            img, 
            caption = "Дешевые авиабилеты, гостиницы и страховки"
                      " в Израиле 🇮🇱 <a href='https://t.me/theisraely/21'>Подробности здесь</a>"
        
        )

    

def register_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start', state = '*')