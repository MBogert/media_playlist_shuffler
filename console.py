import util as u
import playlist

# ==== For handling user I/O ==== #

# Operates off of primitive list-data
def initiate_console_client(media_repo):
    u.print_message(u.INFO, "Initializing Client")
    while True:
        command = str(collect_user_command())
        status = commands[command](media_list = media_repo)
        if status is not True:
            return

def collect_user_command():
    return input('==========================\nWhat would you like to do?\n==========================\nTo create a new playlist, enter \'NEW\'\nTo load an existing playlist, enter \'LOAD\'\nTo terminate the program, enter \'EXIT\'\n')

def exit_program(media_list = []):
    u.print_message(u.INFO, "Terminating console client")
    return False

# || Valid user commands (KEEP AT THE BOTTOM OF THE FILE) || #
# TODO abstract method for command behavior
commands = {
    "NEW": playlist.generate_playlist,
    "LOAD": playlist.load_playlist,
    "EXIT": exit_program,
}