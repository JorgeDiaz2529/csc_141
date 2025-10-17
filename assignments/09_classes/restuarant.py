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