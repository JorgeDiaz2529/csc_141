sandwich_orders = ["Meat", "Pickle", "Pork", "Tuna","Pastrami","Pastrami","Pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrimi.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I have made your {order.lower()} sandwich.")

    finished_sandwiches.append(order)