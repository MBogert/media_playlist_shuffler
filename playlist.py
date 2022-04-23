import os
import random
import shutil
import config as c
import playlist
import util as u
import settings as s

# Clear existing playlist and initialize data for file info...
def bootup():
    clear_playlist()
    return playlist.build_media_repo()

def build_media_repo():
    root = load_root_directory()
    return load_media_files(root)

def clear_playlist():
    try:
        shutil.rmtree(c.PLAYLIST_ROOT)
    except Exception as e:
        u.print_message(u.WARNING, 'Could not clear previous playlist, it may have already been cleaned up')

def generate_playlist(media_list, user_input):
    filepaths = playlist.get_filepaths(media_list, user_input)
    playlist.copy_media(filepaths)

# || Retrieve X number of files within a specified format group
def get_filepaths(media_list, user_input):
    filepaths = []
    supported_formats = s.return_supported_formats(user_input[0])

    counter = user_input[1]
    visited_file_indexes = []
    while counter >= 0:
        # || Retrieve a random file and check if it's a valid format || #
        index = random.randint(0, len(media_list) - 1)
        path = media_list[index]
        if index not in visited_file_indexes and u.is_valid_format(supported_formats, path):
            filepaths.append(path)
            counter -= 1
            visited_file_indexes.append(index)
    return filepaths

# || Take existing files and copy them to a temporary playlist folder || #
# || WARNING: Large files or list sizes can lead to performance/memory issues || #
def copy_media(playlist):
    try:
        os.makedirs(c.PLAYLIST_ROOT)
    except FileExistsError as e:
        u.print_message(u.ERROR, e)
    for media in playlist:
        try:
            shutil.copy2(media, c.PLAYLIST_ROOT)
        except shutil.SameFileError as e:
            u.print_message(u.ERROR, e)
        except PermissionError as e:
            u.print_message(u.ERROR, e)

def load_root_directory():
    root = []
    for file in os.listdir(c.MEDIA_ROOT):
        root.append(c.MEDIA_ROOT + "/" + file)
    return root

def load_media_files(root):
    media_list = []
    while len(root) != 0:
        next_media = root.pop()
        if u.is_directory(next_media):
            for file in os.listdir(next_media):
                root.append(next_media + "/" + file)
        else:
            media_list.append(next_media)
    return media_list