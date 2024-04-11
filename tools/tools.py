import time
import os
import string
import random


from tqdm import tqdm

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import requests
from bs4 import BeautifulSoup

# from pyvirtualdisplay import Display
downloads_folder = 'instagram'
url = 'https://www.instagram.com/reel/C5mGu46LfBB/'

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--headless')
options.add_argument('--no-sandbox')

seleniumwire_options = {'proxy': {
    'http': 'http://zuQ205:Khmw7T@147.45.93.10:8000',
    'https': 'https://zuQ205:Khmw7T@147.45.93.10:8000',
    }}

def generate_random_name():
    characters = string.ascii_letters + string.digits
    random_name = ''.join(random.choice(characters) for _ in range(10))
    return random_name


def get_video(html):
    soup = BeautifulSoup(html, features="html.parser")
    try:
        video = soup.find('video')
        return video['src']
    except Exception as e:
        print(f'src fieled of tag <video> error: {e}')
        return False
    

def save_source_to_file(text):
    with open('source.html', 'w') as file:
        file.write(text)


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
    return file_name


def get_html(url):
    with webdriver.Chrome(
            options=options,
            service=ChromiumService(ChromeDriverManager().install())
        ) as driver:
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                'source': '''
                    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
            '''
            })
            try:
                driver.get(url)
                time.sleep(2)
                html = driver.page_source
                return html
            except Exception as e:
                print(f'Webdriver.get error: {e}')
                return False
            




# html = get_html(url)
# video_url = get_video(html)
# save_source_to_file(html)
# file_name = generate_random_name() + '.mp4'
# download_file_from_url(video_url, file_name, 'video')