import util as u
import bootup
import playlist
import os

# === Miscellaneous Util. Functions === #

# Clear existing playlist data and initialize media data
def bootup_runtime():
    playlist.clear_playlist()
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