
def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            new_args = []
            for a, t in zip(args, types):
                # t(a) for example int('3')
                new_args.append(t(a))
            return f(*new_args, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg("Hello", '3')
