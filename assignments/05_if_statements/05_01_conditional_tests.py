cat_name = "Milo"
cat_color = "Gray"
cat_age = 3

# True statements
print("Is my cat named Milo? I predict true")
print(cat_name == "Milo", "\n")

print("Is my cat gray? I predict true")
print(cat_color == "Gray","\n")

print("Is my cat three? I predict true")
print(cat_age == 3,"\n")

print("Is my cat gray and named Milo? I predict true")
print(True if cat_name == "Milo" and cat_color == "Gray" else False, "\n")

print("Is my cat three and gray? I predict true")
print(True if cat_age == 3 and cat_color == "Gray" else False, "\n")


#False statements
print("Is my cat named John? I predict false")
print(cat_name == "John", "\n")

print("Is my cat yellow? I predict false")
print(cat_color == "Yellow","\n")

print("Is my cat fifty? I predict false")
print(cat_age == 50,"\n")

print("Is my cat yellow and named Milo? I predict false")
print(True if cat_name == "Milo" and cat_color == "Yellow" else False, "\n")

print("Is my cat five and gray? I predict false")
print(True if cat_age == 5 and cat_color == "Gray" else False, "\n")