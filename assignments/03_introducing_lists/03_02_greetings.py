names = ["Johnny","Jorge","Julio"]
messages = ["Hey {name}, how are you?", "Hello, {name}, it's me, you.", "Sup {name}."]

for n in range(3):
    msg = messages[n].format(name = names[n])
    print(msg)