import pytube

def download(url):
    try:
        youtubelink=pytube.YouTube(url)
        video=youtubelink.streams.get_lowest_resolution()
        video.download()
        return True
    except:
        print('Wrong URL')
        return False
    

url = 'https://www.youtube.com/shorts/zgBwy2FrQ9w'

download(url)