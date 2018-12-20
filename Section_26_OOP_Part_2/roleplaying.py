
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def speak(self):
        print("I heard there were monsters running around last night!")
