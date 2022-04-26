import os
import string
import random
import re
import util as u
# || Message Types || #

INFO = 'INFO'
WARNING = 'WARN'
ERROR = 'ERROR'

# || Playlist File 'Format'|| #
PLAYLIST_FORMAT = '.list'

# || Configurable Constants || #
# Root dir of media repository
MEDIA_ROOT = 'media'
# Dir where you want playlist created
PLAYLIST_ROOT = 'playlist_loaded'
# Saved playlist files
SAVED_ROOT = 'saved'
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
    raise Exception('Invalid file format provided: ' + format)

# Print out all saved playlists
def print_saved_playlists():
    for file in os.listdir(u.SAVED_ROOT):
        print_file_playlist(file)

# Print single playlist
def print_file_playlist(file):
    f = open(u.SAVED_ROOT + '\\' + file)
    content = f.read()
    f.close()
    print(file)
    print(content)