favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',}

poll_list = ['sarah', 'jorge', 'genesis', 'yahir']

for person in poll_list:
    if person in favorite_languages:
        print(f"{person.title()} has already taken the poll!")
    else:
        print(f"{person.title()} needs to do the poll!")