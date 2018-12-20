class User:
    # class variable
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))


    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1


    def __repr__(self):
        return  f"{self.first} is {self.age}"

    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has left"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.community}"


print(User.display_active_users())
u1 = User("Tom", "Garcia", 35)
print(User.display_active_users())
jasmine = Moderator("Jasmine", "O'Conner", 61, "Piano")
print(User.display_active_users())

print(jasmine.full_name())
print(jasmine.community)
