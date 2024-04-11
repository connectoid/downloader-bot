from aiogram import Router
from aiogram.types import Message

from tools.tools import get_html, get_video, save_source_to_file, download_file_from_url, generate_random_name

router: Router = Router()


@router.message()
async def get_user_url(message: Message):
    url = message.text
    html = get_html(url)
    video_url = get_video(html)
    save_source_to_file(html)
    file_name = generate_random_name() + '.mp4'
    file_name = download_file_from_url(video_url, file_name, 'video')
    video = open(file_name, "rb")
    await message.send_video(message.chat.id, video = video)