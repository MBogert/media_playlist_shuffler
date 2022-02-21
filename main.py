import playlist
import util as u


# || Runtime || #
def run():
    print('Cleanup on Bootup:')
    playlist.clear_playlist()
    media_repo = playlist.init_media_repo()
    print('Video Repo:')
    u.print_list(media_repo)
    curr_list = playlist.create_playlist(media_repo)
    print('Playlist:')
    u.print_list(curr_list)
    playlist.create_playlist_media(curr_list)


run()
