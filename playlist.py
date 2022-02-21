import os
import random
import shutil
import config as c
import util as u


def init_media_repo():
    traversal_stack = []
    media_list = []
    for file in os.listdir(c.MEDIA_ROOT):
        traversal_stack.append(c.MEDIA_ROOT + "/" + file)
    while len(traversal_stack) != 0:
        next_media = traversal_stack.pop()
        if u.is_directory(next_media):
            for file in os.listdir(next_media):
                traversal_stack.append(next_media + "/" + file)
        else:
            media_list.append(next_media)
    return media_list


def create_playlist(repo):
    playlist = []
    for i in range(c.PLAYLIST_LENGTH):
        index = random.randint(0, len(repo) - 1)
        playlist.append(repo[index])
    return playlist


def create_playlist_media(playlist):
    try:
        os.makedirs(c.PLAYLIST_ROOT)
    except FileExistsError as e:
        u.print_exception(e)
    for media in playlist:
        try:
            shutil.copy2(media, c.PLAYLIST_ROOT)
        except shutil.SameFileError as e:
            u.print_exception(e)
        except PermissionError as e:
            u.print_exception(e)


def clear_playlist():
    try:
        shutil.rmtree(c.PLAYLIST_ROOT)
    except Exception as e:
        u.print_exception(e)
