from time import time
from functools import wraps

def speed_time(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed for {fn.__name__}: {end_time - start_time}")
        return result
    return wrapper

@speed_time
def sum_nums():
    return sum(x for x in range(5000000))

@speed_time
def sum_nums_list():
    return sum([x for x in range(5000000)])

print(sum_nums())
print(sum_nums_list())
