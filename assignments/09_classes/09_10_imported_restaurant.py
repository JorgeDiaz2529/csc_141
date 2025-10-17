from restuarant import Restaurant

pizza_place = Restaurant("Pizzea Place", "Pizza")
pizza_place.increment_number_served(5)

pizza_place.describe_restaurant()
print(pizza_place.number_served)