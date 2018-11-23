# Modeling a playlist

playlist = {
    'title': "patagonia bus",
    "author": "colt steele",
    "songs": [
        {"title":  "song1", "artist": ["blue"], "duration": 2.5},
        {"title":  "song2", "artist": ["kitty", "djcat"], "duration": 5.25},
        {"title":  "meowmeaw", "artist": ["garfield"], "duration": 3.25},
    ]
}

total = 0
for song in playlist['songs']:
    total += song["duration"]

print(total)
