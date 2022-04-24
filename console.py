import util as u
import playlist


# ==== For handling user I/O ==== #

# Operates off of primitive list-data
def initiate_console_client(media_repo):
    u.print_message(u.INFO, "Initializing Client")
    while True:
        user_input = collect_playlist_settings()
        # We assume a non-tuple value to be the 'END' str
        if type(user_input) is not tuple:
            u.print_message(u.INFO, "Terminating Client")
            return
        u.print_message(u.INFO, 'Collecting Media...')
        playlist.generate_playlist(media_repo, user_input)
        u.print_message(u.INFO, 'Playlist ready for use in directory ' + u.PLAYLIST_ROOT)


def collect_playlist_settings():
    end_program = input('Would you like to create a new playlist? (Y/N)')
    if end_program == 'N':
        return 'END'
    format = input('Photo or Video?')
    u.print_message(u.INFO, 'Generating ' + format +'-list')
    file_length = int(input('How many files?'))
    return (format, file_length)

