# create traffic light using itertools

import itertools
import time
import random

colors = 'Red Amber Green'.split()

rotation = itertools.cycle(colors)


def reg_time():
    return random.randint(3, 7)


def rotation_colors():
    for color in colors:
        if color == 'Red':
            print("STOP! the light is {}".format(color))
            time.sleep(reg_time())
        elif color == 'Green':
            print("GO! the light is {}".format(color))
            time.sleep(reg_time())
        else:
            print("CAUTION! the light is {}".format(color))
            time.sleep(reg_time())


rotation_colors()
