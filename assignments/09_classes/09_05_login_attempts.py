class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.user_age = age

        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.user_age} years old.")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
my_user = User("Jorge", "Diaz", 18)

for n in range(3):
    my_user.increment_login_attempts()

print(my_user.login_attempts)

my_user.reset_login_attempts()

print(my_user.login_attempts)
