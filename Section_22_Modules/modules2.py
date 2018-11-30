import keyword

def contains_keyword(*args):
    for word in args:
        if keyword.iskeyword(word):
            return True
    return False

print(contains_keyword("hello", "goodbye") == False)
print(contains_keyword("def" "haha", "lol", "chicken") == True)
print(contains_keyword("four" "haha", "lol", "if") == True)
