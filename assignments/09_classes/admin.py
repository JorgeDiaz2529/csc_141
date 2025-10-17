from user import User
from privileges import Privilege

class Admin(User):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)

        self.privileges = Privilege(["Can ban users", "Can delete posts", "Can mute users"])