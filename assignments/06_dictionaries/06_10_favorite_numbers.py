people = {"Liam": [10, 100, 1000], "Nelly": [99], "Kayla": [50, 250], "Ron": [1, 0], "Shoggorath": [2147483647,-2147483647]}

for person, nums in people.items():
    print(f"{person}'s favorite numbers are: {', '.join(map(str, nums))}")