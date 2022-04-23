import util as u

supported_photo_formats = ['tiff', 'jpeg', 'png', 'gif', 'bmp', 'jpg']
supported_video_formats = ['mp4', 'mov', 'wmv', 'avi', 'qt']

# ==== For handling user I/O ==== #

def collect_input():
    end_program = input('Would you like to create a new playlist? (Y/N)')
    if end_program == 'N':
        u.print_message(u.INFO, 'Okay, terminating program.')
        return ('END')
    format = input('Photo or Video?')
    u.print_message(u.INFO, 'Generating ' + format +'-list')
    file_length = int(input('How many files?'))
    return (format, file_length)

def return_supported_formats(format):
    if format == 'Photo':
        return supported_photo_formats
    elif format == 'Video':
        return supported_video_formats
    raise Exception('Invalid file format provided: ' + format)