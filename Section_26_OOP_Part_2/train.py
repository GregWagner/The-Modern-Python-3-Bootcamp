class Train():

    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return f"{self.num_cars} car train"

    def __len__(self):
        return self.num_cars

t = Train(3)
print(t)
print(len(t))
