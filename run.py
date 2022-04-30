import bootup as b
import console as c
import util as u


# || Runtime || #
def run():
    # || Request console input until terminated ||#
    media_list = b.bootup_runtime()
    c.initiate_console_client(media_list)
    u.print_message(message="Have a nice day!", logging=False)


# || Startup || #
run()
