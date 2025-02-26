import functools

import pytest


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(log_message + "\n")
                print(log_message)

            except Exception as e:
                error_message = (f"{func.__name__} error: {type(e).__name__}."
                                 f" Inputs: {args}, {kwargs}")
                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(error_message + '\n')
                else:
                    print(error_message)

                raise

        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    '''Функция возвращает сумму чисел'''
    return x + y


@log()
def divide(x, y):
    '''Функция возвращает результат деления чисел'''
    if y == 0:
        raise ValueError
    return x / y
