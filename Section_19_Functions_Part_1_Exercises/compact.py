def compact(l):
    return [x for x in l if x]

print(compact([0,1,2,"",[], False, {}, None, "All done"]) == [1,2, "All done"])
