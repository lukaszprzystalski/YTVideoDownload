from pytube import YouTube


link = input("What's the link? \n")
yt = YouTube(link)

print('Titile: ', yt.title)
print('Views: ', yt.views)

yd = yt.streams.get_highest_resolution()
yd.download(r'path to download')