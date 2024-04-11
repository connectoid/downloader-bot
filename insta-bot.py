import requests
import os

from tqdm import tqdm
from bs4 import BeautifulSoup

downloads_folder = 'instagram'

url = 'https://www.instagram.com/tv/C5hqTVQNteQ/?igsh=MWw2Y2JxMGQ4d3h0OQ%3D%3D'
url = 'https://www.instagram.com/reel/C5imClABjZH/'
url = 'https://www.instagram.com/reel/C5mGu46LfBB/?igsh=MXJuOHQ2ODJybzNjaA%3D%3D'
video_url = 'https://scontent.cdninstagram.com/v/t50.16885-16/436362285_829760362501670_3690980981988502543_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=102&_nc_ohc=rfCo_CBezmgAb6RrV3w&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfCYdVZRGdLUZcXZfeLhGSop8BfzkCgk0bYWue7oOEP_IA&oe=6618F062&_nc_sid=10d13b'
video_url = 'https://scontent.cdninstagram.com/v/t66.30100-16/164189920_1901696973596893_7231208721126921715_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=101&_nc_ohc=f4L1HS_dGl4Ab6DK8DY&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfBofVEHayIfQCdHiJt-oqA9yJD2_bBs_s0EuBKle96CEA&oe=6618D292&_nc_sid=10d13b'
video_url = 'https://scontent.cdninstagram.com/v/t66.30100-16/164189920_1901696973596893_7231208721126921715_n.mp4'
video_url = 'https://scontent-ams2-1.cdninstagram.com/v/t66.30100-16/310791442_3270437143265820_4331704922912414379_n.mp4?_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=100&_nc_ohc=RuthyQJppd4Ab6D0LrV&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfBpGzM63sgkdOVh_IY0yxtUiN2xEqKUYkhapHeHcy9SrQ&oe=6618E42D&_nc_sid=10d13b'
import requests

cookies = {
    'csrftoken': 'eLyJV5EgsZUKRdmeXP-U1f',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'csrftoken=eLyJV5EgsZUKRdmeXP-U1f',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.58", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.58"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.2.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'viewport-width': '830',
}

params = {
    'igsh': 'MWs1NDNzNWZsbGp5Ng==',
}

# response = requests.get('https://www.instagram.com/reel/C5imClABjZH/', params=params, cookies=cookies, headers=headers)

def download_file_from_url(url, file_name, dest_folder, chunk_size=128):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_num = tqdm(desc='Downloading File', total=total_size, unit='iB', unit_scale=True)
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)
    if not os.path.exists(f'{downloads_folder}/{dest_folder}'):
        os.makedirs(f'{downloads_folder}/{dest_folder}')
    file_name = f'{downloads_folder}/{dest_folder}/{file_name}'
    with open(file_name, 'wb') as f:
        for data in response.iter_content(chunk_size):
            f.write(data)
            block_num.update(len(data))


def save_source_to_file(text):
    with open('source.html', 'w') as file:
        file.write(text)


def parse_video_url(url):
    response = requests.get(
        url,
        params=params,
        cookies=cookies,
        headers=headers
    )
    save_source_to_file(response.text)
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find_all('div')
    print(len(divs))
    return divs


# download_file_from_url(video_url, 'video.mp4', 'video')

divs = parse_video_url(url)
for div in divs:
    if 'sf-root-media-container' in div:    
        print(div)
    