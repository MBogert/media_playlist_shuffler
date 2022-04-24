import string
import random
import re

# || Message Types || #
INFO = 'INFO'
WARNING = 'WARN'
ERROR = 'ERROR'

# || Configurable Constants || #
# Root dir of media repository
MEDIA_ROOT = 'media'
# Dir where you want playlist created
PLAYLIST_ROOT = 'playlist'
# Change this for longer/shorter filenames
FILENAME_LENGTH = 32
# File formats
SUPPORTED_PHOTO_FORMATS = ['tiff', 'jpeg', 'png', 'gif', 'bmp', 'jpg']
SUPPORTED_VIDEO_FORMATS = ['mp4', 'mov', 'wmv', 'avi', 'qt']



def print_message(level, e):
    print(level + ': ' + str(e))

def is_directory(name):
    return "." not in name

def is_valid_format(formats, path):
    path_format = path.split('.')[-1]
    if path_format in formats:
        return True
    else:
        return False

# Only returns alphabetical characters
def random_filename(format):
    return '/' + ''.join(random.choices(string.ascii_letters, k = FILENAME_LENGTH)) + format

# Returns extension in dot-format
def get_file_extension(filename):
    return re.findall(r'\.[^\.]*$', str(filename))[-1]

def return_supported_formats(format):
    if format == 'Photo':
        return SUPPORTED_PHOTO_FORMATS
    elif format == 'Video':
        return SUPPORTED_VIDEO_FORMATS
    raise Exception('Invalid file format provided: ' + format)