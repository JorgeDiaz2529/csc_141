def make_sandwich(*ingredients):
    print("The sandwich will have:")
    for i in ingredients:
        print(i)
    print()

make_sandwich("Pickles")
make_sandwich("Lettuce", "Tomato")
make_sandwich("Cheese", "Chicken", "Steak")