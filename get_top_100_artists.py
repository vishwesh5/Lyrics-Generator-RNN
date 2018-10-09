import requests

url = 'https://itunes.apple.com/us/rss/topsongs/limit=100/json'

response = requests.get(url)

data = response.json()

f_art = open("artists.txt",'w')
f_songs = open("songs.txt",'w')

for artist_dict in data['feed']['entry']:
    artist_name = artist_dict['im:artist']['label']
    song_artist = artist_dict['title']['label']
    song,artist = song_artist.split(" - ")
    #f_art = open("artists.txt",'w')
    #f_songs = open("songs.txt",'w')
    f_art.write(artist+"\n")
    f_songs.write(song+"\n")
    #print(song,artist)
f_art.close()
f_songs.close()
