
def copy_and_reverse(filename, new_file):
    with open(filename) as orig:
        text = orig.read()
    with open(new_file, 'w') as new:
        new.write(text[::-1])
