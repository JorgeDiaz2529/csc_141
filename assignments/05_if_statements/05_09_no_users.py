usernames = ["Admin","Lorem","Ipsum","Sorem","Delta"]

for name in usernames:
    if name == "Admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}")

usernames = []

if len(usernames) == 0:
    print("We need to find some users!")