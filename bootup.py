import util as u
import os
import shutil
from datetime import datetime

# === Functions for program setup === #

# Build/check project structure, and load media files to data
def bootup_runtime():
    init_project()
    if len(os.listdir(u.MEDIA_ROOT)) == 0:
        u.print_message(message='Media directory empty, exiting program, goodbye')
        quit()
    else:
        return build_media_data()


# Returns a list of all filepaths/dirpaths in the media repo
def build_media_data():
    # Check if a file is already loaded
    root = []
    with open(u.MEDIA_LIB, "r+") as f:
        if len(f.readlines()) > 0:
            if input('File loaded, use it? (if media library has been modified, update recommended)') == 'n':
                for file in os.listdir(u.MEDIA_ROOT):
                    f.truncate(0)
                    root.append(u.MEDIA_ROOT + "/" + file)
                    f.write(u.MEDIA_ROOT + "/" + file + '\n')
            else:
                root = f.readlines()
        else:
            for file in os.listdir(u.MEDIA_ROOT):
                root.append(u.MEDIA_ROOT + "/" + file)
                f.write(u.MEDIA_ROOT + "/" + file + '\n')
        f.close()
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
def init_project():
    # Create project structure for runtime
    # Logfile (archive previous log)
    u.create_directory(u.LOGS_ROOT)
    shutil.copy2(u.LOG_FILE, u.random_filename(u.LOG_FILE)[1:])
    u.create_file(filename=u.LOG_FILE, overwrite=True)
    # Loaded playlists
    u.create_directory(u.PLAYLIST_ROOT)
    u.create_directory(u.PLAYLIST_ROOT_PHOTO)
    u.create_directory(u.PLAYLIST_ROOT_VIDEO)
    # Saved playlist files
    u.create_directory(u.SAVED_ROOT)
    # Media playlist
    u.create_directory(u.MEDIA_ROOT)
    # End
    u.print_message(message='Project structure initialized', console=False)
    return True
