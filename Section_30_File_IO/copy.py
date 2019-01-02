
def copy(filename, new_file):
    with open(filename) as orig:
        with open(new_file, 'w') as new:
            new.write(orig.read())

