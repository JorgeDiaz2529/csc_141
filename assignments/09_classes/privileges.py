class Privilege:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"The admin can do the following:")
        for privilege in self.privileges:
            print(privilege)