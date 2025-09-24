people = [{"first name": "John", "last name": "Ham", "age": 500, "city": "Rome"},
          {"first name": "Sam", "last name": "Smith", "age": 20, "city": "Reading"},
          {"first name": "Josue", "last name": "Miguel", "age": 22, "city": "Baltimore"}]

for p in people:
    print(f"{p["first name"]} {p["last name"]} is {p["age"]} years old and lives in {p["city"]}.")


