pets = [{"animal": "cat", "owner": "john"},
        {"animal": "dog", "owner": "don"},
        {"animal": "penguin", "owner": "ron"}]

for pet in pets:
    print(f"{pet["owner"].title()} owns a {pet["animal"].title()}!")
