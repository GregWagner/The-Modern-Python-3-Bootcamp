users = [
    {"username": "samuel", "tweets": []},
    {"username": "katie", "tweets": []},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": []},
    {"username": "guitar_gal", "tweets": []}
]

#new_users = sorted(users, key=lambda user: len(user['tweets']))
new_users = sorted(users, key=lambda user: user['username'])
for user in new_users:
    print(user)

