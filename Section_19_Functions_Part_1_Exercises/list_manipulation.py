def list_manipulation(l, cmd, loc, value=0):
    if cmd == "remove" and loc == "end":
        return l.pop()
    if cmd == "remove" and loc == "beginning":
        return l.pop(0)
    if cmd == "add" and loc == "beginning":
        l.insert(0, value)
        return l
    if cmd == "add" and loc == "end":
        l.append(value)
        return l

print(list_manipulation([1,2,3], "remove", "end") == 3)
print(list_manipulation([1,2,3], "remove", "beginning") == 1)
print(list_manipulation([1,2,3], "add", "beginning", 20))
#==  [20,1,2,3])
print(list_manipulation([1,2,3], "add", "end", 30) ==  [1,2,3,30])

