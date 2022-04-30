import os
import random
import shutil
import util as u
import re

# === For handling playlist data === #

# || Builds a randomized media playlist || #
# || Takes a list of filepaths/dirpaths, and a tuple of user settings for the playlist || #
def generate_playlist(media_list = []):
    if len(os.listdir(u.MEDIA_ROOT)) == 0:
        u.print_message(level=u.INFO, message='Media directory is empty, please load appropriate media')
        return True
    user_input = collect_playlist_settings()
    # Clear existing playlist data and copy new media over
    u.print_message(message = 'Generating playlist of ' + str(user_input[1]) + ' ' + str(user_input[0]))
    filepaths = get_filepaths(media_list, user_input)
    clear_playlist()
    copy_media(filepaths)
    # Save new playlist to file, and store in 'saved' dir
    playlist_name = str(create_playlist_file(filepaths))
    u.print_message(message = 'Playlist generated, saving to file: ' + playlist_name)
    return True

# || Retrieve X number of files within a specified format group, based on user_input || #
def get_filepaths(media_list, user_input):
    filepaths = []
    # || Ask for media formats (or short circuit on error) || #
    supported_formats = u.return_supported_formats(user_input[0])
    if len(supported_formats) == 0:
        return []
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
    u.print_message(message = 'Filepaths retrieved: ' + str(filepaths), console = False)
    return filepaths

# || Take existing files and copy them to a temporary playlist folder || #
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
        u.print_message(message='Playlist queue cleared', console = False)
    except Exception as e:
        u.print_message(u.WARNING, 'Could not clear previous playlist, it may have already been cleaned up', console = False)

def collect_playlist_settings():
    format = input('Photo or Video?\n')
    file_length = int(input('How many files?\n'))
    return (format, file_length)

# || Clears existing playlist and loads new media from file || #
def load_playlist(media_list = []):
    filename = select_playlist_file()
    u.print_message(message='Loading playlist file: ' + filename)
    loaded_playlist = load_playlist_file(u.SAVED_ROOT + '\\' + filename)
    if loaded_playlist != []:
        clear_playlist()
        copy_media(loaded_playlist)
        u.print_message(message='Media successfully loaded!')
    else:
        u.print_message(message='Playlist data not found')
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
    try:
        file = open(filename, 'r')
        media_data = file.read()[1:-1].replace('\'', '').split(', ')
        media_list = []
        for media in media_data:
            media_list.append(media)
        return media_list
    except FileNotFoundError as e:
        u.print_message(level=u.ERROR, message='File not found: ' + filename)
        return []

def select_playlist_file():
    if print_saved_playlists() is True:
        return input('Enter the playlist\'s filename, which you would like to load, all saved playlists are displayed above...\n')
    else:
        u.print_message(level=u.WARNING, message='No playlist files identified in ' + u.SAVED_ROOT)
        return ''

# Print out all saved playlists
# Returns status whether or not files exist
def print_saved_playlists():
    if len(os.listdir(u.SAVED_ROOT)) > 0:
        for file in os.listdir(u.SAVED_ROOT):
            print_playlist_file(file)
        return True
    else:
        u.print_message(u.VIEW, message='==== ==== ====\nNo playlist files identified\n==== ==== ====', logging=False)
        return False


# Print single playlist
def print_playlist_file(file):
    u.print_message(u.VIEW, '===== Playlist =====', logging=False)
    with open(u.SAVED_ROOT + '\\' + file, 'r') as f:
        content = f.read()[1:-1].replace('\'', '').split(', ')
        u.print_message(u.VIEW, 'Name: ' + f.name + '\n' + 'Files: ' + str(len(content)), logging=False)
        for media in content:
            u.print_message(u.VIEW, media, logging=False)
        f.close()
    u.print_message(u.VIEW, '==== ==== ==== ==== ====\n', logging=False)


# Print playlist currently loaded up
def print_loaded_playlist(media_list=[]):
    u.print_message(level=u.VIEW, message='===== Current Playlist =====', logging=False)
    for file in os.listdir(u.PLAYLIST_ROOT):
        u.print_message(level=u.VIEW, message=file, logging=False)
    u.print_message(u.VIEW, '==== ==== ==== ====\n', logging=False)
    return True

# || Runs the current playlist in `loaded_playlist` || #
def run_current_playlist():
    try:
        if len(os.listdir(u.PLAYLIST_ROOT)) > 0:
            os.startfile(os.path.normpath(u.PLAYLIST_ROOT ))
        else:
            u.print_message(u.WARNING, 'Media files not identified in ' + u.PLAYLIST_ROOT)
    except FileNotFoundError as e:
        u.print_message(level = u.ERROR, message = str(e))