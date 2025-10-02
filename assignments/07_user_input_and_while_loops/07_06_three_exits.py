prompt = "Please enter what topping you'd like for your pizza!\nOr enter 'quit' to exit!\n"

msg = ""
active = True
while active == True:
    msg = input(prompt)

    if msg == "quit":
        active == False
        break