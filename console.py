import util as u
import playlist as p
import command as c


# ==== For handling user I/O ==== #

# The crucial method for program runtime
def initiate_console_client(media_repo):
    u.print_message(message="Initializing Client")
    while True:
        command = str(collect_user_command())
        try:
            status = commands[command](media_list=media_repo)
        except KeyError as e:
            u.print_message(level=u.WARNING, message='Invalid command received: ' + command)
            status = True
        # False status is an exit state for the client
        if status is not True:
            return
        else:
            # Check if user wants to run the currently loaded playlist
            if confirm_playlist_run() is True:
                p.run_current_playlist()


def collect_playlist_settings():
    format = input('Photo or Video?\n')
    file_length = int(input('How many files?\n'))
    return (format, file_length)


def collect_user_command():
    return input(
        '==========================\nWhat would you like to do?\n==========================\nTo create a new playlist, enter \'NEW\'\nTo load an existing playlist, enter \'LOAD\'\nTo view the currently loaded playlist, enter \'VIEW\'\nTo terminate the program, enter \'EXIT\'\n')


def confirm_playlist_run():
    confirm_run = input('Would you like to run the currently loaded playlist?(Y/N)')
    return True if confirm_run == 'Y' else False


def select_playlist_file():
    if p.print_saved_playlists() is True:
        return input(
            'Enter the playlist\'s filename, which you would like to load, all saved playlists are displayed above...\n')
    else:
        u.print_message(level=u.WARNING, message='No playlist files identified in ' + u.SAVED_ROOT)
        return ''


# || Valid user commands (KEEP AT THE BOTTOM OF THE FILE) || #
# || Methods used below must have the minimum structure (media_list = []) || #
commands = {
    "NEW": c.generate_playlist,
    "LOAD": c.load_playlist,
    "VIEW": c.print_loaded_playlist,
    "EXIT": c.exit_program,
}
