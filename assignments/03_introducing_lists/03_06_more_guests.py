guest_list = ["Lilian", "Jorge", "Kristel"]

for guest in guest_list:
    print(f"Hello {guest}, you are invited to dinner.")

print("\nA bigger table was found!\n")

guest_list.insert(0,"Josue")
guest_list.insert(2, "Raul")
guest_list.append("Jose")

for guest in guest_list:
    print(f"Hello {guest}, you are invited to dinner.")