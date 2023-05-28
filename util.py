import string
import random
import re
from datetime import datetime
import os
import shutil

# || Message Types || #
INFO = 'INFO'
WARNING = 'WARN'
ERROR = 'ERROR'
VIEW = 'VIEW'

# || Custom File Types || #
PHOTO_FORMAT = '.Photo'
VIDEO_FORMAT = '.Video'

# || Configurable Constants || #
# Root dir of media repository
MEDIA_ROOT = 'media'
# Dir where you want playlist created
PLAYLIST_ROOT = 'playlist_loaded'
PLAYLIST_ROOT_VIDEO = 'playlist_loaded/video/'
PLAYLIST_ROOT_PHOTO = 'playlist_loaded/photo/'
# Saved playlist files
SAVED_ROOT = 'saved'
# Log file
LOGS_ROOT = 'logs/'
LOG_FILE = 'log_file.log'
# Change this for longer/shorter filenames
FILENAME_LENGTH = 32

# File formats
SUPPORTED_PHOTO_FORMATS = ['tiff', 'jpeg', 'png', 'gif', 'bmp', 'jpg']
SUPPORTED_VIDEO_FORMATS = ['mp4', 'mov', 'wmv', 'avi', 'qt']

# Index Variables for playlist settings tuple (see console.py -> collect_playlist_settings())
SETTINGS_INDEX_FORMAT = 0
SETTINGS_INDEX_LENGTH = 1


def print_message(level=INFO, message='', console=True, logging=True):
    if console is True:
        print(level + ': ' + str(message))
    if logging is True:
        with open(LOG_FILE, 'a') as f:
            f.write('||' + str(datetime.now()) + '||: ' + level + ': ' + message + '\n')
            f.close()


def is_directory(name):
    return "." not in name


# Checks if a given filepath contains a compatible format
def is_valid_format(formats, path):
    if '.' not in path:
        return False
    path_format = path.split('.')[-1]
    if path_format in formats:
        return True
    else:
        return False


# Only returns alphabetical characters
# Requires format specified
def random_filename(filename):
    return '/' + ''.join(random.choices(string.ascii_letters, k=FILENAME_LENGTH)) + get_file_format(filename)


# Returns extension in dot-format
def get_file_format(filename):
    return '' if '.' not in filename else re.findall(r'\.[^\.]*$', str(filename))[-1]


def return_supported_formats(file_format):
    if file_format == PHOTO_FORMAT:
        return SUPPORTED_PHOTO_FORMATS
    elif file_format == VIDEO_FORMAT:
        return SUPPORTED_VIDEO_FORMATS
    else:
        print_message(level=WARNING, message='Invalid format identified: ' + file_format)
        return []


def print_files_for_directory(dirpath, header='======== Playlist ========', footer=' === === ===   === === ===\n'):
    print_message(level=VIEW, message=header, logging=False)
    for file in os.listdir(dirpath):
        print_message(level=VIEW, message=file, logging=False)
    print_message(level=VIEW, message=footer, logging=False)

# Create a directory
def create_directory(dirpath):
    try:
        os.makedirs(dirpath)
        print_message(message='Directory created: ' + dirpath, console=False)
    except FileExistsError as e:
            print_message(message='Directory exists', console=False)

# Create a file
# For overwriting a file, set `overwrite=True`
def create_file(filename, overwrite=False):
    try:
        with open(filename, 'a') as f:
            if overwrite is True:
                f.truncate(0)
            else:
                u.print_message(message='File initialized: ' + filename, console=False)
    except {IOError, FileNotFoundError} as e:
        u.print_message(message='Error initializing file: ' + filename, console=False)
