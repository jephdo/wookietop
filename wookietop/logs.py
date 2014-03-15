import time
import functools
from collection import deque

def coroutine(func):
    @functools.wrap
    def wrapper(*args, **kwargs):
        cr = func()
        # python2 uses `next` and python3 uses `__next__`
        try:
            cr.__next__()
        except AttributeError:
            cr.next()

        return cr
    return wrapper

def search_file(filename):
    pass

def ls(path):
    pass



def tail(log_file, target, interval=2):
    log_file.seek(0, 2) # go to the end of the file

    while True:
        line = log_file.readline()
        if not line:
            time.sleep(interval)
            continue

        target.send(line)

@coroutine
def sink():
    while True:
        line = (yield)
        # emit(line)
