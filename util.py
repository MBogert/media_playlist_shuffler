import os
import string
import random
import re
import util as u
from datetime import datetime
# || Message Types || #

INFO = 'INFO'
WARNING = 'WARN'
ERROR = 'ERROR'
VIEW = 'VIEW'

# || Playlist File 'Format'|| #
PLAYLIST_FORMAT = '.list'

# || Configurable Constants || #
# Root dir of media repository
MEDIA_ROOT = 'media'
# Dir where you want playlist created
PLAYLIST_ROOT = 'playlist_loaded'
# Saved playlist files
SAVED_ROOT = 'saved'
# Log file
LOG_FILE = 'log_file.log'
# Change this for longer/shorter filenames
FILENAME_LENGTH = 32
# File formats
SUPPORTED_PHOTO_FORMATS = ['tiff', 'jpeg', 'png', 'gif', 'bmp', 'jpg']
SUPPORTED_VIDEO_FORMATS = ['mp4', 'mov', 'wmv', 'avi', 'qt']

def print_message(level = u.INFO, message = '', console = True, logging = True):
    if console is True:
        print(level + ': ' + str(message))
    if logging is True:
        with open(u.LOG_FILE, 'a') as f:
            f.write('||' + str(datetime.now()) + '||: ' + level + ': ' + message + '\n')
            f.close()

def is_directory(name):
    return "." not in name

def is_valid_format(formats, path):
    path_format = path.split('.')[-1]
    if path_format in formats:
        return True
    else:
        return False

# Only returns alphabetical characters
# Requires format specified
def random_filename(filename):
    return '/' + ''.join(random.choices(string.ascii_letters, k = FILENAME_LENGTH)) +  get_file_extension(filename)

# Returns extension in dot-format
def get_file_extension(filename):
    return re.findall(r'\.[^\.]*$', str(filename))[-1]

def return_supported_formats(format):
    if format == 'Photo':
        return SUPPORTED_PHOTO_FORMATS
    elif format == 'Video':
        return SUPPORTED_VIDEO_FORMATS
    else:
        print_message(level = u.WARNING, message = 'Invalid format identified: ' + format)
        return []

# Print out all saved playlists
def print_saved_playlists():
    for file in os.listdir(u.SAVED_ROOT):
        print_playlist_file(file)

# Print single playlist
def print_playlist_file(file):
    print_message(u.VIEW, '===== Playlist =====', logging = False)
    with open(u.SAVED_ROOT + '\\' + file, 'r') as f:
        content = f.read()[1:-1].replace('\'', '').split(', ')
        print_message(u.VIEW, 'Name: ' + f.name + '\n' + 'Files: ' + str(len(content)), logging = False)
        for media in content:
            print_message(u.VIEW, media, logging = False)
        f.close()
    print_message(u.VIEW, '===== ===== =====\n', logging=False)