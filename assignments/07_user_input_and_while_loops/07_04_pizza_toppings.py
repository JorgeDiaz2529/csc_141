prompt = "Please enter what topping you'd like for your pizza!\nOr enter 'quit' to exit!\n"

msg = ""
while msg != "quit":
    msg = input(prompt)

    if msg == "quit":
        break