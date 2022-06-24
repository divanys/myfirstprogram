import youtube_dl
import os.path
def download_mp4(url):
  info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
  file_name = f"{info['title']}.mp4"
  options = {
  'format': 'best',
  'outtmpl': file_name,
  }
  if os.path.exists(f'{file_name}'):
    os.remove(f'{file_name}')
  with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])

media = input()

download_mp4(media)