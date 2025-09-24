users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'bio': "Yo. I love science and stuff.",
        'online': True
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'bio': "Chemicals.",
        'online': False
        },
    }

for username, user_info in users.items():

    print(f"\nUsername: {username}")

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print('\t' + user_info['bio'])

    if user_info['online']:
        print(f'\t{full_name} is online!')
    else:
        print(f'\t{full_name} is offline')