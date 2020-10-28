# DECORATORS
from functools import wraps
import time


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('our wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


class decorator_class(object):  # some people also like to use a Class as a decorator
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))

    return wrapper


# @decorator_function  # Class decorator instead of a function decorator
# def display():
#     print('display function ran')


@my_logger  # this is and...
@my_timer  # ...this
def display_info(name, age):
    time.sleep(1)
    print('display_info fan with arguments ({}, {})'.format(name, age))


# display_info = my_logger(my_timer(display_info))  # are equal to this

# decorator_display = decorator_function(display)


# display()
display_info('Hank', 30)
