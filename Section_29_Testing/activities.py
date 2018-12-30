import random

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise(ValueError("is_healthy must be a boolean"))

    if is_healthy:
        ending = "because my body is a temple"
    else:
        ending = "because you only live once"
    return f"I'm eating {food}, " + ending

def nap(nap_time):
    if nap_time < 2:
        return f"I'm feeling refreshed after my {nap_time} hour nap"
    else:
        return f"Ugh, I overselpt. I didn't mean to nap {nap_time} hours"

def is_funny(name):
    if name is "tim":
        return False
    return True

def laugh():
    return random.choice(['lol', 'haha', 'tehehe'])
