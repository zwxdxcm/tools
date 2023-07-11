"""
Miscellaneous helper code.
"""
import datetime
import random
import string
import os
import time
from collections.abc import Iterator
import psutil
import sys

def gen_cur_time():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


def gen_random_string(n=4):
    return "".join(random.sample(string.ascii_letters + string.digits, n))


# decorator
def time_cost(func):
    def _time_cost(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print("==> time-cost: %6f (s)     %s " % (time.time() - start, func.__name__))
        return ret

    return _time_cost


def gen_random_mark(nums=4):
    return "".join(random.choice(string.ascii_lowercase) for i in range(nums))


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024.0 / 1024
    print("{} memory used: {} MB".format(hint, memory))


def get_var_memo_size(var):
    return sys.getsizeof(var)


def is_iterator(obj):
    return isinstance(obj, Iterator)


def gen_common_color(idx=0):
    # BGR MODE
    colors = (
        (255, 0, 0),  # Blue
        (0, 0, 255),  # Red
        (0, 255, 0),  # Green
        (0, 255, 255),  # Yellow
        (255, 255, 0),  # Cyan
        (255, 0, 255),  # Magenta
        (128, 128, 128),  # Gray
        (192, 192, 192),  # Silver
        (0, 0, 128),  # Maroon
        (0, 128, 128),  # Olive
        (128, 0, 0),  # Navy
        (128, 128, 0),  # Teal
        (128, 0, 128),  # Purple
        (0, 128, 255),  # Orange
        (0, 215, 255),  # Gold
        (0, 51, 153),  # Brown
        (255, 218, 185),  # Peach
        (114, 128, 250),  # Salmon
        (220, 245, 245),  # Beige
        (250, 230, 230),  # Lavender
        (208, 224, 64),  # Turquoise
        (250, 255, 127),  # Mint
        (140, 230, 240),  # Khaki
        (130, 0, 75),  # Indigo
        (255, 0, 200),  # Fuchsia
        (235, 206, 135),  # SkyBlue
        (205, 90, 106),  # SlateBlue
        (55, 140, 45),  # ForestGreen
    )

    return colors[idx % len(colors)]