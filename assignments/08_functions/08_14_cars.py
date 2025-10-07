def make_car(manafacturer, model, **car_info):
    car_info['manafacturer'] = manafacturer
    car_info['model'] = model
    return car_info

car = make_car("BMW", "BMW X6", color="Red", used=False)
print(car)