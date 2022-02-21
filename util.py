import config as c


def print_list(list_val):
    print('List Value:', *list_val, sep=c.PRINT_FORMAT)


def print_exception(e):
    print('ERROR: ' + str(e))


def is_directory(name):
    return "." not in name

