from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age if age > 0 else 0

#   def get_age(self):
#       return self._age

#   def set_age(self, new_age):
#       self._age = new_age if new_age > 0 else 0

    def __repr__(self):
        return f"Human named {self.full_name}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        raise TypeError("Both must be Humans")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Can't multiply"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age if new_age > 0 else 0

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


jane = Human("Jane", "Goodall", -9)
print(jane.age)
print(jane)
jane.age = 45
print(jane.age)
print(jane.full_name)
jane.full_name = "Greg Wagner"
print(jane.full_name)

keven = Human("Kevin", "Jones", 49)
print(keven + jane)
print(jane * 3)
print((keven + jane) * 3)

