from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from misc.owm import Owm
from misc.currency_converter import CurrencyMixins
from misc.photo_generator.generator import PhotoGenerator
from app.config import BOT_TOKEN, API_KEY


# aiogram
bot = Bot(token=BOT_TOKEN, parse_mode = 'html')
storage = MemoryStorage()
dp = Dispatcher(bot, storage = storage)


# Open weather map api
owm = Owm(API_KEY)


# Currencies and Cryptocurrency
cur = CurrencyMixins()

# Photo generator class
pg = PhotoGenerator()


# Apscheduler
scheduler = AsyncIOScheduler()