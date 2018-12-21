# wraps perserves a function's metadata when it is decorated
from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I am wrapper function"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    """Adds two number together."""
    return x + y

print(add(1, 2))

# NOTE: help(add) give the wrapper function help - not the help for add unless
# you use wraps from functools
help(add)
