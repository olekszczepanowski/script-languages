import logging
import functools
import time

def log (level=logging.DEBUG):
    logging.basicConfig(level=level)
    def decorator (func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            startTime = time.time()
            result = func(*args, **kwargs)
            endTime = time.time()
            duration = endTime - startTime
            logging.log(level, f"Funkcja '{func.__name__}' wywołana z args: {args}, kwargs: {kwargs}")
            logging.log(level, f"Funkcja '{func.__name__}' zwrociła: {result}")
            logging.log(level, f"Funkcja '{func.__name__}' wykonała się w: {duration} sekund")
            return result
        return wrapper
    return decorator

@log(level=logging.DEBUG)
def example_function(x, y):
    return x + y

@log(level=logging.DEBUG)
class ExampleClass:
    def __init__(self, name):
        self.name = name

example_function(3, 5)
example_instance = ExampleClass("example")