from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config import BOT_TOKEN, API_KEY, API_SECRET
from app.connection import Database
from misc.mail_sender.sender import SendMail

# aiogram
bot = Bot(token=BOT_TOKEN, parse_mode = 'html')
storage = MemoryStorage()
dp = Dispatcher(bot, storage = storage)

# DataBase
db = Database()

# Email
email_sender = SendMail(API_KEY, API_SECRET)