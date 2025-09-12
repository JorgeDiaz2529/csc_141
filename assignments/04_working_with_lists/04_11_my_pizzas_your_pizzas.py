pizzas = ["Cheese","Pepperoni","Chicken"]

# for pizza in pizzas:
#     print(f"I love {pizza} pizza!")

# print("I love the taste of cheese on my pizza!\nI love the addition of pepperoni on my pizza\n" \
# "I love topping my pizza with chicken!\nI really love pizza!")

friend_pizzas = pizzas[:]
friend_pizzas.append("Mushroom")
friend_pizzas.remove("Chicken")

print("My favorite pizzas are:")
for p in pizzas:
    print(p)

print("\nMy friends favorite pizzas are:")
for p in friend_pizzas:
    print(p)