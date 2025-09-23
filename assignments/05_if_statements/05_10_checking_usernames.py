current_users = ["jogn", "all5", "2zsl","halqw","jazz"]
new_users = ["john","Jazz","All3","Meh20888","Aster"]

for user in new_users:
    if user.lower() in current_users:
        print("Username unavailable, please input another one.")
    else:
        print("Username is available!")
