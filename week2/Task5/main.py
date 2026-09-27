events = {
    "City walking tour": "18.09.2026",
    "Painting class": "18.09.2026",
    "Museum tour": "19.09.2026",
    "Photo exhibition": "19.09.2026",
    "Art workshop": "19.09.2026",
    "Football exhibition": "20.09.2026",
    "Film night": "20.09.2026",
    "Book presentation": "21.09.2026",
    "Science exhibition": "22.09.2026",
    "Architecture tour": "23.09.2026",
    "Craft workshop": "24.09.2026",
    "Music workshop": "25.09.2026",
    "Art market": "26.09.2026"
}

print("Events on 19.09.2026:")

for event, date in events.items():
    if date == "19.09.2026":
        print(event)