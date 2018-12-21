from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args: {}:".format(args))
        print("Here are the kwargs: {}:".format(kwargs))
        fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3, a="hi", b="bye")
