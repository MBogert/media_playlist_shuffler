import os
import random
import shutil
import util as u
import re


# === For handling playlist data === #

# || Retrieve random media based on user input (file_type, num_files) || #
def get_filepaths(media_list, user_input):
    filepaths = []
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
    u.print_message(message='Filepaths retrieved: ' + str(filepaths), console=False)
    return filepaths


# || Take existing files and copy them to a temporary playlist folder || #
# || WARNING: Large files or list sizes can lead to performance/memory issues || #
def copy_media(playlist, format):
    path = u.PLAYLIST_ROOT_VIDEO if format == 'Video' else u.PLAYLIST_ROOT_PHOTO
    for media in playlist:
        try:
            shutil.copy2(media, path)
            # Randomize filenames to 'break up' adjacent media by source
            filename = re.findall(r'/[^//]*$', str(media))[-1]
            os.rename(path + filename, path + u.random_filename(filename))
        except Exception as e:
            u.print_message(u.ERROR, e)


# Removes existing media in playlist repo
def clear_playlist(format):
    if format == 'Photo':
        try:
            shutil.rmtree(u.PLAYLIST_ROOT_PHOTO)
            os.makedirs(u.PLAYLIST_ROOT_PHOTO)
            u.print_message(message='Photo queue cleared', console=False)
        except Exception as e:
            print('Error in clearing photo dir')
    if format == 'Video':
        try:
            shutil.rmtree(u.PLAYLIST_ROOT_VIDEO)
            os.makedirs(u.PLAYLIST_ROOT_VIDEO)
            u.print_message(message='Video queue cleared', console=False)
        except Exception as e:
            print('Error in clearing video dir')


# Writes playlist to file for later use, and moves to 'saved' directory
# Non-zero (but miniscule) chance of duplicate filenames
def create_playlist_file(media_list, format):
    file = open(u.random_filename('.' + format)[1:], 'w')
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


# Print out all playlists saved to file
def print_saved_playlists():
    if len(os.listdir(u.SAVED_ROOT)) > 0:
        for file in os.listdir(u.SAVED_ROOT):
            print_playlist_file(file)
        return True
    else:
        u.print_message(u.VIEW, message='==== ==== ====\nNo playlist files identified\n==== ==== ====', logging=False)
        return False


# Print single playlist from file
def print_playlist_file(file):
    u.print_message(u.VIEW, '===== Playlist =====', logging=False)
    with open(u.SAVED_ROOT + '\\' + file, 'r') as f:
        content = f.read()[1:-1].replace('\'', '').split(', ')
        u.print_message(u.VIEW, 'Name: ' + f.name + '\n' + 'Files: ' + str(len(content)), logging=False)
        for media in content:
            u.print_message(u.VIEW, media, logging=False)
        f.close()
    u.print_message(u.VIEW, '==== ==== ==== ==== ====\n', logging=False)


# || Runs the current playlist in `loaded_playlist` || #
def run_loaded_playlist():
    format = input('Load Photo or Video?\n')
    try:
        dir = u.PLAYLIST_ROOT_VIDEO if format == 'Video' else u.PLAYLIST_ROOT_PHOTO
        if len(os.listdir(dir)) > 0:
            os.startfile(os.path.normpath(dir))
        else:
            u.print_message(u.WARNING, 'Media files not identified in ' + dir)
    except FileNotFoundError as e:
        u.print_message(level=u.ERROR, message=str(e))
