import settings

from environs import Env


env = Env()
env.read_env()

if settings.DUBUG:
    BOT_TOKEN = env.str("DEV_BOT_TOKEN")
    GROUP_ID = env.str("DEV_GROUP_ID")
    RECIPIENT_GMAIL = env.str("DEV_RECIPIENT_GMAIL")

else:
    BOT_TOKEN = env.str("BOT_TOKEN")
    GROUP_ID = env.str("GROUP_ID")
    RECIPIENT_GMAIL = env.str("RECIPIENT_GMAIL")


CHANNEL_ID = env.str("CHANNEL_ID")
ADMINS = env.list("ADMINS")


# Mailjet Api (Send mail)
API_KEY = env.str("API_KEY")
API_SECRET = env.str("API_SECRET")