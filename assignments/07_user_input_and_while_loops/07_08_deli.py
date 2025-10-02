sandwich_orders = ["Meat", "Pickle", "Pork", "Tuna"]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I have made your {order.lower()} sandwich.")

    finished_sandwiches.append(order)