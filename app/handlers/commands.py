from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from loader import bot, db
from app import buttons


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()

    user = message.from_user
    if not db.get_expert(user.id):
        await message.answer(
            "Добрый день. Вас приветствует электронный помощник "
            "цифрового сервиса «предложить проект». Пройдите регистрацию, "
            "чтобы выступать в качестве эксперта и оценивать инвестиционные "
            "проекты (инициативы) предложенные к реализации в Хабаровском крае.",
            reply_markup = buttons.apply_btns()
        )
    elif db.get_expert(user.id).status == 'approved':
        await message.answer("Оцените, пожалуйста, инвестиционные проекты",
            reply_markup = buttons.show_projects()
        )
    elif db.get_expert(user.id).status == 'pending':
        await message.answer("Вас уже подали на заявку. Ждите ответа от модераторов.")
    

def register_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start', state = '*')

