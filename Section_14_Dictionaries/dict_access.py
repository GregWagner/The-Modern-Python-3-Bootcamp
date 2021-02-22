from random import choice

food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear",
               "tea cake"])

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

print(f"Looking for {food}")

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")
