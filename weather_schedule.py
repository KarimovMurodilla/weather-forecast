from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.config import GROUP_ID

from loader import bot
from misc.photo_generator.generator import PhotoGenerator

scheduler = AsyncIOScheduler()
pg = PhotoGenerator()

async def send_current_weather():
    image = pg.put_all_info_on_photo()

    with open(image, 'rb') as img:
        await bot.send_photo(GROUP_ID, img, caption = "Text")


    
def schedule_jobs():
    scheduler.add_job(send_current_weather, 'interval', minutes=1)