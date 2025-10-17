class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine}")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ["Vanilla", "Chocolate", "Mint", "Cookies & Cream"]
    
    def display_flavors(self):
        print(self.flavors)

icecream_stand = IceCreamStand("Joe's Cream", "Ice Cream")
icecream_stand.display_flavors()
    