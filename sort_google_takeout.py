import eyed3
import time

from os import listdir, makedirs, rename
from os.path import isfile, join, exists

def build_album_path(audiofile, base_dir):
    return base_dir + "/" + audiofile.tag.artist + "/" + audiofile.tag.album

def build_album_directory(album_directory):
    if not exists(album_directory):
        makedirs(album_directory)

def build_song_path(album_directory, audiofile):
    track = audiofile.tag.track_num
    track_num = str(track[0]) if track[0] >= 10 else "0" + str(track[0]) 
    
    return album_directory + "/" + str(track_num) + "." + audiofile.tag.title + ".mp3"


def move_song_to(song_path, target_path):
    try:
        rename(song_path, target_path)
    except Exception:
        print("skip " + song_path)


music_directory  = "Takeout/gpmusique/Titres/"


onlyfiles = [join(music_directory, f) for f  in listdir(music_directory) if isfile(join(music_directory, f)) and f.endswith(".mp3") ]



for song in onlyfiles:
    audiofile_metadata = eyed3.load(song)
    album_dir_path = build_album_path(audiofile_metadata, "/home/khantzen/music/all")
    build_album_directory(album_dir_path)

    song_path = build_song_path(album_dir_path, audiofile_metadata)
    move_song_to(song, song_path)

