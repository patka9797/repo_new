from time import time

def my_decorator(func):
    def decorated_func(*args, **kwargs):
        start = start.time()
        result = func(*args, **kwargs)
        end = end.time()
        runtime = end - start

    return decorated_func

@my_decorator
def sleep_function():
    time.sleep(15)
    print('Im sleeping right now')

result = sleep_function
