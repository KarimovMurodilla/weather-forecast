import pytz

from app.config import GROUP_ID
from loader import bot, pg, scheduler


async def send_current_weather():
    image = pg.put_all_info_on_photo()

    with open(image, 'rb') as img:
        await bot.send_photo(
            GROUP_ID, 
            img, 
            caption = "Дешевые авиабилеты, гостиницы и страховки"
                      " в Израиле 🇮🇱 <a href='https://t.me/theisraely/21'>Подробности здесь</a>"
        
        )


    
def schedule_jobs():
    scheduler.add_job(send_current_weather, trigger='cron', hour='14', minute='20', timezone=pytz.timezone('Israel'))
    # scheduler.add_job(send_current_weather, trigger='cron', hour='15', timezone=pytz.timezone('Israel'))
    # scheduler.add_job(send_current_weather, trigger='cron', hour='19', timezone=pytz.timezone('Israel'))