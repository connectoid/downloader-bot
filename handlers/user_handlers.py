import os
from dotenv import load_dotenv

from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.types import (CallbackQuery, Message, ReplyKeyboardRemove, 
                           LabeledPrice, PreCheckoutQuery, ContentType)

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

router = Router()
bot = Bot(BOT_TOKEN, parse_mode='HTML')

# @router.message(~F.text)
# async def content_type_example(msg: Message):
#     await msg.answer('👍')


@router.message(CommandStart())
async def process_start_command(message: Message):
    tg_id = message.from_user.id
    await message.answer(
        text=f'Здравствуйте! Вы запустили бот для для загрузки видео из Инстаграм. Отправьте мне ссылку на видео.',
    )
