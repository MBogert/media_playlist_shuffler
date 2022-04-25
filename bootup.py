import util as u
import bootup
import os

# === Miscellaneous Util. Functions === #

# Build project structure and initialize media data
def bootup_runtime():
    if init_project() is not True:
        u.print_message(u.INFO, 'Please add media to the appropriate directory, and re-boot the program, thank you')
        return []
    else:
        media_repo = bootup.build_media_repo()
        u.print_message(u.INFO, 'Bootup Complete!')
        return media_repo

# Returns a list of all filepaths/dirpaths in the media repo
def build_media_repo():
    root = []
    for file in os.listdir(u.MEDIA_ROOT):
        root.append(u.MEDIA_ROOT + "/" + file)
    return load_media_files(root)

# For use in bootup, collects all filepaths/dirpaths in media directory
# Returned in list data-format
def load_media_files(root):
    media_list = []
    while len(root) != 0:
        next_media = root.pop()
        if u.is_directory(next_media):
            for file in os.listdir(next_media):
                root.append(next_media + "/" + file)
        else:
            media_list.append(next_media)
    return media_list

# Creates necessary project structure
# Returns a bool value
#   True => Project is fully built
#   False => Error, or additional setup required
def init_project():
    # Check if media repo is loaded
    try:
        os.makedirs(u.MEDIA_ROOT)
        u.print_message(u.INFO, 'Empty media repo initialized')
        # User needs to populate media repo
        return False
    except FileExistsError as e:
        u.print_message(u.INFO, 'Media repo has already been initialized')
    # Playlist
    try:
        os.makedirs(u.PLAYLIST_ROOT)
    except FileExistsError as e:
        u.print_message(u.INFO, 'Playlist repo has already been initialized')
    # Saved Playlists
    try:
        os.makedirs(u.SAVED_ROOT)
    except FileExistsError as e:
        u.print_message(u.INFO, 'Saved repo has already been initialized')
    # End
    u.print_message(u.INFO, 'Project structure initialized')
    return True