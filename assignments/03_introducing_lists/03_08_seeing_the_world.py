locations = ["Guatemala, London", "Japan", "Paris", "Home"]

print(locations)
print(f"Sorted: {sorted(locations)}")
print(f"Original: {locations}")
print(f"Reverse-Sorted: {sorted(locations, reverse=True)}\n")

locations.reverse()
print(locations)
# back to normal...
locations.reverse()
print(f"{locations}\n")

locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)