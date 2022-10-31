from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()


async def send_current_weather():
    pass


    
def schedule_jobs():
    scheduler.add_job(send_current_weather, 'interval', minutes=1)
