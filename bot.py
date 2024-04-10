from pytube import YouTube

def get_video(url):
    try:
        yt = YouTube(url)
        for stream in yt.streams:
            print(stream.resolution)
        # video=yt.streams.get_lowest_resolution()
        # video.download()
        return True
    except:
        print('Wrong URL')
        return False
    

url = 'https://www.youtube.com/shorts/zgBwy2FrQ9w'
url = 'https://www.youtube.com/watch?v=2EZ5Z6mBEa8'

get_video(url)