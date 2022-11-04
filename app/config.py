import settings

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
GROUP_ID = env.str("GROUP_ID")
ADMINS = env.str("ADMINS")

API_KEY = env.str("API_KEY")