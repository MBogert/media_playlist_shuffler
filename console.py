import util as u
import playlist

# ==== For handling user I/O ==== #

# Operates off of primitive list-data
def initiate_console_client(media_repo):
    u.print_message(message = "Initializing Client")
    while True:
        command = str(collect_user_command())
        try:
            status = commands[command](media_list = media_repo)
        except KeyError as e:
            u.print_message(level = u.WARNING, message = 'Invalid command received: ' + command)
            status = True
        # False status is an exit state for the client
        if status is not True:
            return

def collect_user_command():
    return input('==========================\nWhat would you like to do?\n==========================\nTo create a new playlist, enter \'NEW\'\nTo load an existing playlist, enter \'LOAD\'\nTo view the currently loaded playlist, enter \'VIEW\'\nTo terminate the program, enter \'EXIT\'\n')

def exit_program(media_list = []):
    u.print_message(message = "Terminating Client", console = False)
    return False

# || Valid user commands (KEEP AT THE BOTTOM OF THE FILE) || #
commands = {
    "NEW": playlist.generate_playlist,
    "LOAD": playlist.load_playlist,
    "VIEW": u.print_loaded_playlist,
    "EXIT": exit_program,
}