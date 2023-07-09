"""
Miscellaneous helper code.
"""
import datetime
import random
import string

def gen_cur_time():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


def gen_random_string(n=4):
    return "".join(random.sample(string.ascii_letters + string.digits, n))