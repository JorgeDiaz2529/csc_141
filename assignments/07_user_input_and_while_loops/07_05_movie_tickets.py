prompt = "Hello customer, how old are you?\nEnter 'quit' to leave the program\n"

age = ""
while age != "quit":
    age = input(prompt)
    
    if age == "quit":
        break
    
    age = int(age)

    if age < 3:
        print("Your ticket is free!")
    elif age >= 3 and age < 12:
        print("Your ticket will be $10!")
    elif age >= 12:
        print("Your ticket will be $15!") 