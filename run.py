import bootup
import console
import util as u

# || Runtime || #
def run():
    # || Request console input until terminated ||#
    media_list = bootup.bootup_runtime()
    console.initiate_console_client(media_list)
    u.print_message(u.INFO, "Have a nice day!")

# || Startup || #
run()