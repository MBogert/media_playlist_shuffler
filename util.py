import config as c

# || Message Types || #
INFO = 'INFO'
WARNING = 'WARN'
ERROR = 'ERROR'

# === Miscellaneous Util. Functions === #

def print_message(level, e):
    print(level + ': ' + str(e))

def is_directory(name):
    return "." not in name

def is_valid_format(formats, path):
    path_format = path.split('.')[1]
    if path_format in formats:
        return True
    else:
        return False