import logging

from aiogram import Bot, executor
from aiogram.types import BotCommand

from app.handlers.commands import register_cmd_handlers

from loader import bot, dp
from weather_schedule import scheduler, schedule_jobs


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать бота")
    ]
    await bot.set_my_commands(commands)


async def main(dp):
    logging.basicConfig(level=logging.INFO)

    register_cmd_handlers(dp)
    
    await set_commands(bot)
    schedule_jobs()
    

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup = main)

