import util as u
import playlist as p
import os
import console as c


# || Holds the method calls useds in console.py, under 'commands' || #
# || All methods must take at least 1 list-parm named 'media_list' ||#

# NEW
def generate_playlist(media_list=[]):
    if len(os.listdir(u.MEDIA_ROOT)) == 0:
        u.print_message(level=u.INFO, message='Media directory is empty, please load appropriate media')
        return True
    user_input = c.collect_playlist_settings()
    # Clear existing playlist data and copy new media over
    u.print_message(message='Generating playlist of ' + str(user_input[1]) + ' ' + str(user_input[0]))
    filepaths = p.get_filepaths(media_list, user_input)
    p.clear_playlist(user_input[0])
    p.copy_media(filepaths, user_input[0])
    # Save new playlist to file, and store in 'saved' dir
    playlist_name = str(p.create_playlist_file(filepaths, user_input[0]))
    u.print_message(message='Playlist generated, saving to file: ' + playlist_name)
    return True


# LOAD
def load_playlist(media_list=[]):
    filename = c.select_playlist_file()
    format = u.get_file_format(filename)
    u.print_message(message='Loading playlist file: ' + filename)
    loaded_playlist = p.load_playlist_file(u.SAVED_ROOT + '\\' + filename)
    print(loaded_playlist)
    if loaded_playlist:
        p.clear_playlist(format)
        p.copy_media(loaded_playlist, format[1:])
        u.print_message(message='Media successfully loaded!')
    else:
        u.print_message(message='Playlist data not found')
    return True


# VIEW
def print_loaded_playlists(media_list=[]):
    # Video
    u.print_files_for_directory(u.PLAYLIST_ROOT_VIDEO)
    # Photo
    u.print_files_for_directory(u.PLAYLIST_ROOT_PHOTO)
    return True


# EXIT
def exit_program(media_list=[]):
    u.print_message(message="Terminating Client", console=False)
    return False

# RUN
def run_loaded_playlist(media_list=[]):
    format = input('Load Photo or Video?\n')
    try:
        dir = u.PLAYLIST_ROOT_VIDEO if format == 'Video' else u.PLAYLIST_ROOT_PHOTO
        if len(os.listdir(dir)) > 0:
            os.startfile(os.path.normpath(dir))
        else:
            u.print_message(u.WARNING, 'Media files not identified in ' + dir)
    except FileNotFoundError as e:
        u.print_message(level=u.ERROR, message=str(e))
    return True