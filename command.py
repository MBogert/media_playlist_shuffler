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
    p.clear_playlist()
    p.copy_media(filepaths)
    # Save new playlist to file, and store in 'saved' dir
    playlist_name = str(p.create_playlist_file(filepaths))
    u.print_message(message='Playlist generated, saving to file: ' + playlist_name)
    return True


# LOAD
def load_playlist(media_list=[]):
    filename = p.select_playlist_file()
    u.print_message(message='Loading playlist file: ' + filename)
    loaded_playlist = p.load_playlist_file(u.SAVED_ROOT + '\\' + filename)
    if loaded_playlist:
        p.clear_playlist()
        p.copy_media(loaded_playlist)
        u.print_message(message='Media successfully loaded!')
    else:
        u.print_message(message='Playlist data not found')
    return True


# VIEW
def print_loaded_playlist(media_list=[]):
    u.print_message(level=u.VIEW, message='===== Current Playlist =====', logging=False)
    for file in os.listdir(u.PLAYLIST_ROOT):
        u.print_message(level=u.VIEW, message=file, logging=False)
    u.print_message(u.VIEW, '==== ==== ==== ==== ====\n', logging=False)
    return True


# EXIT
def exit_program(media_list=[]):
    u.print_message(message="Terminating Client", console=False)
    return False
