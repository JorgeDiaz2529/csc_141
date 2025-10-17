class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine}")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant_1 = Restaurant("John's Chicken", "Chicken")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("Sam's Sandwichery", "Sandwiches")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("The Pizzaria", "Pizza")
restaurant_3.describe_restaurant()