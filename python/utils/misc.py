import random
import string
import datetime

def gen_random_string(n=4):
    return "".join(random.sample(string.ascii_letters + string.digits, n))

def gen_random_mark(nums=4):
    return "".join(random.choice(string.ascii_lowercase) for i in range(nums))

def gen_cur_time():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")