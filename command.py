import util as u
import playlist as p
import os
import console as c
import random as r

# || Holds the method calls useds in console.py, under 'commands' || #
# || All methods must take at least 1 list-parm named 'media_list' ||#

# NEW
def generate_playlist(media_list=[]):
    if len(os.listdir(u.MEDIA_ROOT)) == 0:
        u.print_message(level=u.INFO, message='Media directory is empty, please load appropriate media')
        return True
    user_input = c.collect_playlist_settings()
    # Clear existing playlist data and load new media
    u.print_message(message='Generating playlist of ' + str(user_input[u.SETTINGS_INDEX_LENGTH]) + ' ' + str(user_input[u.SETTINGS_INDEX_FORMAT]))
    filepaths = p.get_filepaths(media_list, user_input)
    p.clear_playlist(user_input[u.SETTINGS_INDEX_FORMAT])
    p.copy_media(filepaths, user_input[u.SETTINGS_INDEX_FORMAT])
    # Save new playlist to file, and store in 'saved' dir
    playlist_name = str(p.create_playlist_file(filepaths, user_input[u.SETTINGS_INDEX_FORMAT]))
    u.print_message(message='Playlist generated, saving to file: ' + playlist_name)
    return True


# LOAD
def load_playlist(media_list=[]):
    filename = c.select_playlist_file()
    file_format = u.get_file_format(filename)
    u.print_message(message='Loading playlist file: ' + filename)
    loaded_playlist = p.load_playlist_file(u.SAVED_ROOT + '\\' + filename)
    if loaded_playlist:
        p.clear_playlist(file_format)
        p.copy_media(loaded_playlist, file_format)
        u.print_message(message='Media successfully loaded!')
    else:
        u.print_message(message='Playlist data not found')
    return True


# VIEW
def print_loaded_playlists(media_list=[]):
    # Video
    u.print_message(level=u.VIEW, message='========  .Video  ========', logging=False)
    u.print_files_for_directory(u.PLAYLIST_ROOT_VIDEO)
    # Photo
    u.print_message(level=u.VIEW, message='========  .Photo  ========', logging=False)
    u.print_files_for_directory(u.PLAYLIST_ROOT_PHOTO)
    return True


# EXIT
def exit_program(media_list=[]):
    u.print_message(message="Terminating Client", console=False)
    return False

# RUN
def run_loaded_playlist(media_list=[]):
    file_format = input('Load Photo or Video?\n')
    try:
        dir = u.PLAYLIST_ROOT_VIDEO if file_format == 'Video' else u.PLAYLIST_ROOT_PHOTO
        if len(os.listdir(dir)) > 0:
            os.startfile(os.path.normpath(dir))
        else:
            u.print_message(u.WARNING, 'Media files not identified in ' + dir)
    except FileNotFoundError as e:
        u.print_message(level=u.ERROR, message=str(e))
    return True

# RND (Load random file w/o generating a playlist)
def run_random_media(media_list=[]):
    file=''
    while True: # Randomly iterate through media util an appropriate file is found
        file = media_list[r.randint(0, len(media_list))]
        if u.is_valid_format(u.return_supported_formats(u.VIDEO_FORMAT), file):
            break
    try:
        os.startfile(os.path.normpath(file))
        u.print_message(level=u.INFO, message='Loading random media: ' + file, console=False)
    except FileNotFoundError as e:
        u.print_message(level=u.ERROR, message=str(e))
    return True