# GitHub: https://github.com/wh0th3h3llam1
# Author: wh0th3h3llam1

import os

os.system("")

# Group of Different functions for different styles
class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(Color.YELLOW + "Hello, World!")


# REFERENCES:
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                formatting = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (formatting, formatting)
            print(s1)
        print('\n')

print_format_table()
