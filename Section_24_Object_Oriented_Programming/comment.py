class Comment:

    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

c = comment("greg", "this is a test")
c1 = comment("fred", "This is also a test", 3)
