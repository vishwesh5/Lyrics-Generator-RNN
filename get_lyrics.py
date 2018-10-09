import lyricwikia

f_art = open("artists.txt",'r')
f_songs = open("songs.txt",'r')
f_art_mod = open("artists_found.txt",'w')
f_songs_mod = open("songs_found.txt",'w')
f_lyrics = open("lyrics.txt",'w')

artists_list = f_art.readlines()
songs_list = f_songs.readlines()

for i in range(len(artists_list)):
    artist = artists_list[i].strip("\n")
    song = songs_list[i].strip("\n")
    print("[INFO] Processing song: {}, artist: {}".format(song,artist))
    try:
        lyrics = lyricwikia.get_lyrics(artist,song)
        f_lyrics.write(lyrics+"\n")
        f_art_mod.write(artist+"\n")
        f_songs_mod.write(song+"\n")
    except:
        print("[ERROR] Song: {}, Artist: {} NOT FOUND".format(song,artist))

f_art.close()
f_songs.close()
f_art_mod.close()
f_songs_mod.close()
f_lyrics.close()
