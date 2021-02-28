import time


def time_work(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        a = func(*args, **kwargs)
        print("--- %s seconds ---" % (time.time() - start_time))
        return a
    return wrapper


def get_time_work(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        return (time.time() - start_time)
    return wrapper
