import sys

age = input("Enter your age: ")

if not age:
    print('Please enter an age')
    sys.exit()

age = int(age)
if age < 18:
    print("You can't come in, little one")
elif age < 21:
    print("You can enter, but you need a wristbad")
else:
    print("You are good to enter and can drink")
