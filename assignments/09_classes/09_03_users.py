class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.user_age = age
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.user_age} years old.")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

my_user = User("Jorge", "Diaz", 18)
my_user.describe_user()
my_user.greet_user()

new_user = User("Lorem","Ipsum", 3000)
new_user.describe_user()
new_user.greet_user()