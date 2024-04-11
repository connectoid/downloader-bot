import os
from dotenv import load_dotenv

from aiogram import Bot, Router
from aiogram.types import Message
from tools.tools import get_html, get_video, save_source_to_file, download_file_from_url, generate_random_name

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

router: Router = Router()
bot = Bot(BOT_TOKEN, parse_mode='HTML')

@router.message()
async def get_user_url(message: Message):
    url = message.text
    print(f'Recieved link {url}')
    html = get_html(url)
    if html:
        print(f'Recieved html')
        video_url = get_video(html)
        if video_url:
            print(f'Recieved video url')
            save_source_to_file(html)
            file_name = generate_random_name() + '.mp4'
            file_name = download_file_from_url(video_url, file_name, 'video')
            print(f'File {file_name} saved')
            video = open(file_name, "rb")
            await message.answer(text=f'File {file_name} saved')
            await bot.send_video(message.chat.id, video = video)
        else:
            await message.answer(text=f'Ошибка при получении ссылки на видео')
    else:
        await message.answer(text=f'Неправильная ссылка')
