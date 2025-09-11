guest_list = ["Lilian", "Jorge", "Kristel"]

for guest in guest_list:
    print(f"Hello {guest}, you are invited to dinner.")

print("\nA bigger table was found!\n")

guest_list.insert(0,"Josue")
guest_list.insert(2, "Raul")
guest_list.append("Jose")

for guest in guest_list:
    print(f"Hello {guest}, you are invited to dinner.")

print("\nI can only invite two people!\n")

for n in range(len(guest_list)):
    if n >= 2:
        guest_list.pop()

for guest in guest_list:
    print(f"{guest} is still invited!")

guest_list.pop()
guest_list.pop()

print(guest_list)