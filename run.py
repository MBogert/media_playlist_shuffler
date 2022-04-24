import bootup
import console

# || Runtime || #
def run():
    # || Request console input until terminated ||#
    media_list = bootup.bootup_runtime()
    console.initiate_console_client(media_list)

# || Startup || #
run()