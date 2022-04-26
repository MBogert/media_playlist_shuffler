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
    # Clear existing playlist data and copy new media over
    u.print_message(u.INFO, 'Generating playlist')
    filepaths = get_filepaths(media_list, user_input)
    clear_playlist()
    copy_media(filepaths)
    # Save new playlist to file, and store in 'saved' dir
    u.print_message(u.INFO, 'Playlist generated, saving to file')
    playlist_name = str(create_playlist_file(filepaths))
    u.print_message(u.INFO, 'Written to ' + playlist_name)
    return True

# Retrieve X number of files within a specified format group, based on user_input
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
    for media in playlist:
        try:
            shutil.copy2(media, u.PLAYLIST_ROOT)
            # Randomize filenames to 'break up' adjacent media by source
            filename = re.findall(r'/[^//]*$', str(media))[-1]
            os.rename(u.PLAYLIST_ROOT + filename, u.PLAYLIST_ROOT + u.random_filename(filename))
        except Exception as e:
            u.print_message(u.ERROR, e)

def clear_playlist():
    try:
        shutil.rmtree(u.PLAYLIST_ROOT)
        os.makedirs(u.PLAYLIST_ROOT)
    except Exception as e:
        u.print_message(u.WARNING, 'Could not clear previous playlist, it may have already been cleaned up')

def collect_playlist_settings():
    format = input('Photo or Video?\n')
    u.print_message(u.INFO, 'Generating ' + format +'-list')
    file_length = int(input('How many files?\n'))
    return (format, file_length)

# Clears existing playlist and loads new media from file
def load_playlist(media_list = []):
    filename = select_playlist_file()
    loaded_playlist = load_playlist_file(u.SAVED_ROOT + '\\' + filename)
    clear_playlist()
    u.print_message(u.INFO, 'Playlist queue cleared')
    copy_media(loaded_playlist)
    u.print_message(u.INFO, 'Media successfully loaded')
    return True

# Writes playlist to file for later use, and moves to 'saved' directory
# Non-zero (but miniscule) chance of duplicate filenames
def create_playlist_file(media_list):
    file = open(u.random_filename('file.list')[1:], 'w')
    file.write(str(media_list))
    file.close()
    shutil.move(file.name, u.SAVED_ROOT + '/' + file.name)
    return file.name

# Takes a playlist file (.list) and returns the data in list format
def load_playlist_file(filename):
    file = open(filename, 'r')
    media_data = file.read()[1:-1].replace('\'', '').split(', ')
    media_list = []
    for media in media_data:
        media_list.append(media)
    return media_list

def select_playlist_file():
    u.print_saved_playlists()
    return input('Enter the playlist\'s filename, which you would like to load, all saved playlists are displayed above...\n')
