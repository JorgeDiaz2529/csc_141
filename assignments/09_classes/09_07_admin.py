class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.user_age = age
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.user_age} years old.")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

class Admin(User):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)

        self.privileges = ["Can ban users", "Can delete posts", "Can mute users"]
    
    def show_privileges(self):
        print(f"The admin {self.first_name} can do the following:")
        for privilege in self.privileges:
            print(privilege)

admin = Admin("Sam", "Adminer", 67)
admin.show_privileges()

    