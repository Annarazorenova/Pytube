import pytube

video_link = r'https://www.youtube.com/watch?v=Z1maCxwkwjg'


yt = pytube.YouTube(video_link)
streams = yt.streams
video_best = streams.order_by('resolution').desc().first()
audio_best = streams.filter(only_audio=True).desc().first()
print(video_best)
path = 'C:\Downloads'
video_best.download(path)
audio_best.download(path)