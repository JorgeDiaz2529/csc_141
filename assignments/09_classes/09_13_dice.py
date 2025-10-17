from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        result = randint(1,self.sides)
        print(f"d{self.sides} rolled: {result}")

d6 = Die()
for i in range(10):
    d6.roll_dice()

print()

d10 = Die(10)
for i in range(10):
    d10.roll_dice()

print()

d20 = Die(20)
for i in range(10):
    d20.roll_dice()
