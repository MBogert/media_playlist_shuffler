import util as u
import os


# === Functions for program setup === #

# Build/check project structure, and load media files to data
def bootup_runtime():
    if init_project() is not True:
        u.print_message(message='Please add media to the appropriate directory, and re-boot the program, thank you',
                        logging=False)
        return []
    else:
        media_repo = build_media_data()
        u.print_message(message='Bootup Complete!')
        return media_repo


# Returns a list of all filepaths/dirpaths in the media repo
def build_media_data():
    root = []
    for file in os.listdir(u.MEDIA_ROOT):
        root.append(u.MEDIA_ROOT + "/" + file)
    return load_media_files(root)


# For use in bootup, collects all filepaths from the media root directory, and returns in list-format
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
# Returns bool value based on init status
def init_project():
    # Log-file
    with open(u.LOG_FILE, 'a') as f:
        f.truncate(0)
    u.print_message(message='Logfile initialized: ' + u.LOG_FILE, console=False)
    # Media files repository
    try:
        os.makedirs(u.MEDIA_ROOT)
        u.print_message(message='Empty media repo initialized: ' + u.MEDIA_ROOT, console=False)
    except FileExistsError as e:
        u.print_message(message='Media repo has already been initialized', console=False)
    # Holding dir for loaded playlists
    try:
        os.makedirs(u.PLAYLIST_ROOT)
        u.print_message(message='Playlist root: ' + u.PLAYLIST_ROOT, console=False)
    except FileExistsError as e:
        u.print_message(message='Playlist repo has already been initialized', console=False)
    # Photo
    try:
        os.makedirs(u.PLAYLIST_ROOT_PHOTO)
        u.print_message(message='Playlist photo root: ' + u.PLAYLIST_ROOT_PHOTO, console=False)
    except FileExistsError as e:
        u.print_message(message='Photo playlist repo has already been initialized', console=False)
    # Video
    try:
        os.makedirs(u.PLAYLIST_ROOT_VIDEO)
        u.print_message(message='Playlist video root: ' + u.PLAYLIST_ROOT_VIDEO, console=False)
    except FileExistsError as e:
        u.print_message(message='Video playlist repo has already been initialized', console=False)
    # Saved playlists files repo (.list)
    try:
        os.makedirs(u.SAVED_ROOT)
        u.print_message(message='Saved playlist repo initialized: ' + u.SAVED_ROOT, console=False)
    except FileExistsError as e:
        u.print_message(message='Saved playlist repo has already been initialized', console=False)
    # End
    u.print_message(message='Project structure initialized', console=False)
    return True
