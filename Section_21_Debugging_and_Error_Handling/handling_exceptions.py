try:
    foobar
except NameError as err:
    print(err)

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Ricky"}
print(get(d, "Fred"))
print(get(d, "name"))

while True:
    try:
        num = int(input("Please enter an number: "))
    except ValueError as err:
        print("That is not a number")
    else:
        print("Input was success")
        break
    finally:
        print("I always run")
print("Rest of game logic")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except TypeError:
        print("both values must be numbers")
    else:
        print(f"{a} / {b} = {result}")
        return result

print(divide(1, 2))
print(divide(1, 'a'))
