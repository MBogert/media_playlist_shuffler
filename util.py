import string
import random
import re
from datetime import datetime
import os

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
PLAYLIST_ROOT_VIDEO = '/playlist_loaded/video/'
PLAYLIST_ROOT_PHOTO = '/playlist_loaded/photo/'
# Saved playlist files
SAVED_ROOT = 'saved'
# Log file
LOG_FILE = 'log_file.log'
# Change this for longer/shorter filenames
FILENAME_LENGTH = 32
# File formats
SUPPORTED_PHOTO_FORMATS = ['tiff', 'jpeg', 'png', 'gif', 'bmp', 'jpg']
SUPPORTED_VIDEO_FORMATS = ['mp4', 'mov', 'wmv', 'avi', 'qt']


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
    return re.findall(r'\.[^\.]*$', str(filename))[-1]


def return_supported_formats(format):
    if format == 'Photo':
        return SUPPORTED_PHOTO_FORMATS
    elif format == 'Video':
        return SUPPORTED_VIDEO_FORMATS
    else:
        print_message(level=WARNING, message='Invalid format identified: ' + format)
        return []


def print_files_for_directory(dirpath, header='======== Playlist ========', footer='==== ==== ==== ==== ====\n'):
    print_message(level=VIEW, message=header, logging=False)
    for file in os.listdir(dirpath):
        print_message(level=VIEW, message=file, logging=False)
    print_message(level=VIEW, message=footer, logging=False)