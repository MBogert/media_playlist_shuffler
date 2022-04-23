import playlist
import settings as settings
import config as c
import util as u

# || Runtime || #
def run():
    media_list = playlist.bootup()
    u.print_message(u.INFO, 'Bootup Complete!')

    # || Request console input until terminated ||#
    while True:
        user_input = settings.collect_input()
        if user_input[0] == 'END':
            break
        u.print_message(u.INFO, 'Collecting Media...')
        playlist.generate_playlist(media_list, user_input)
        u.print_message(u.INFO, 'Playlist ready for use in directory ' + c.PLAYLIST_ROOT)

# || Startup || #
run()