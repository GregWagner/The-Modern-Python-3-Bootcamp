def calculate(make_float, operation, first, second, message="The result is"):
    if operation == "add":
        result = first + second
    elif operation == "subtract":
        result = first - second
    elif operation == "multiply":
        result = first * second
    elif operation == "divide":
        result = first / second
    if make_float:
        return message + ' ' + str(float(result))
    else:
        return message + ' ' + str(int(result))


# You just added 6
print(calculate(make_float=False, operation='add', message='You just added',
                first=2, second=4))

# "The result is 0.7"
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
