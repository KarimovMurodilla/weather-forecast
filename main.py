import logging

from aiogram import Bot, executor
from aiogram.types import BotCommand

from loader import bot
from misc.scheduler import scheduler, weather_schedule


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать бота")
    ]
    await bot.set_my_commands(commands)


async def main(dp):
	logging.basicConfig(level=logging.INFO)

	await set_commands(bot)

    schedule_jobs()


if __name__ == '__main__':
    scheduler.start()
	executor.start_polling(dp, on_startup = main)

