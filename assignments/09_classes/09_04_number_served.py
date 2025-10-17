class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine}")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")
    
    def set_number_served(self, n):
        self.number_served = n

    def increment_number_served(self, n):
        self.number_served += n


taco_place = Restaurant("Taquito's", "Taquitos")
print(taco_place.number_served)

taco_place.set_number_served(30)
print(taco_place.number_served)

taco_place.increment_number_served(5)
print(taco_place.number_served)