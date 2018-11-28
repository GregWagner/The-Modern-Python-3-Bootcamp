def colorize(text, color):
    colors = ("cyan", "yellow", "green", "magenta")

    if type(text) is not str:
        raise TypeError("text must be instance of string")
    if type(color) is not str:
        raise TypeError("color must be instance of string")
    if color not in colors:
        raise ValueError("color is an unknown color")
    print(f"Printed {text} in {color}")

colorize(10, "red")
