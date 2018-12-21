from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [result, result]
    return wrapper


@double_return
def add(x, y):
    return x + y

@double_return
def greet(name):
    return "Hi, I'm " + name

print(add(1, 2))
print(greet("Colt"))
