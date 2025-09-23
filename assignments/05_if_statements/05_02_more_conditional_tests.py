cat_name = "Milo"
cat_color = "Gray"
cat_age = 3

name_list = ["Mike", "Cheezer", "Fluffles"]

print(f"Is cat gray: {cat_color == "Gray"}")
print(f"Is cat NOT gray: {cat_color != "Gray"}")
print(f"Is cat named Milo: {cat_name.lower() == "milo"}")
print(f"Is cat older than 4: {cat_age > 4}")
print(f"Is cat older or equal to 3: {cat_age >= 3}")
print(f"Is cat younger than 10: {cat_age < 10}")
print(f"Is cat 3 years old AND gray: {cat_age == 3 and cat_color == "Gray"}")
print(f"Is cat named Milo or Mike: {cat_name == "Milo" or cat_name == "Mike"}")
print(f"Is cat Milo in list: {cat_name in name_list}")
print(f"Is cat Milo NOT in list: {cat_name not in name_list}")
