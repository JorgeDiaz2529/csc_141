guest_list = ["Lilian", "Jorge", "Kristel"]

for guest in guest_list:
    print(f"Hello {guest}, you are invited to dinner.")

print("Jorge couldn't make it")
guest_list[1] = "Raul"

for guest in guest_list:
    print(f"Hello {guest}, you are invited to dinner.")