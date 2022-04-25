import os
import random
import shutil
import util as u
import re

# === For handling playlist data === #

# Builds a randomized media playlist
# Takes a list of filepaths/dirpaths, and a tuple of user settings for the playlist
def generate_playlist(media_list = []):
    user_input = collect_playlist_settings()
    u.print_message(u.INFO, 'Generating playlist')
    filepaths = get_filepaths(media_list, user_input)
    copy_media(filepaths)
    u.print_message(u.INFO, 'Process complete')
    return True

# Retrieve X number of files within a specified format group
def get_filepaths(media_list, user_input):
    filepaths = []
    supported_formats = u.return_supported_formats(user_input[0])
    counter = user_input[1]
    visited_file_indexes = []
    while counter > 0:
        # || Retrieve a random file and check if it's a valid format || #
        index = random.randint(0, len(media_list) - 1)
        path = media_list[index]
        if index not in visited_file_indexes and u.is_valid_format(supported_formats, path):
            filepaths.append(path)
            counter -= 1
            visited_file_indexes.append(index)
    u.print_message(u.INFO, 'Filepaths retrieved')
    return filepaths

# Take existing files and copy them to a temporary playlist folder
# || WARNING: Large files or list sizes can lead to performance/memory issues || #
def copy_media(playlist):
    try:
        os.makedirs(u.PLAYLIST_ROOT)
    except FileExistsError as e:
        u.print_message(u.ERROR, e)
    for media in playlist:
        try:
            shutil.copy2(media, u.PLAYLIST_ROOT)
            # Randomize filenames to 'break up' adjacent media by source
            filename = re.findall(r'/[^//]*$', str(media))[-1]
            os.rename(u.PLAYLIST_ROOT + filename, u.PLAYLIST_ROOT + u.random_filename(u.get_file_extension(filename)))
        except shutil.SameFileError as e:
            u.print_message(u.ERROR, e)
        except PermissionError as e:
            u.print_message(u.ERROR, e)

# TODO Use for DELETE command
# Removes all current files in playlist directory
def clear_playlist():
    try:
        shutil.rmtree(u.PLAYLIST_ROOT)
    except Exception as e:
        u.print_message(u.WARNING, 'Could not clear previous playlist, it may have already been cleaned up')
    finally:
        os.makedirs(u.PLAYLIST_ROOT)
        u.print_message(u.INFO, 'Initialized empty playlist directory')

def collect_playlist_settings():
    format = input('Photo or Video?')
    u.print_message(u.INFO, 'Generating ' + format +'-list')
    file_length = int(input('How many files?'))
    return (format, file_length)

def load_playlist(media_list = []):
    return True