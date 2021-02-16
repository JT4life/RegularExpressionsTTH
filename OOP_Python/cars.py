class Car:
    # class attributes
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, model, year, make='Ford'):
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        self.gas = 100

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True

    def stop(self):
        if self.is_moving:
            print("Car has stopped")
            self.is_moving = False
        else:
            print("Car already stopped")

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print("The car starts moving")
                self.is_moving = True
            print(f'The car is going {speed}')
        else:
            print("You have run out of gas")
            self.stop()


class Dealership:
    def __init__(self):
        # self.cars = ["Ford Focus", "Honda Civic", "Toyota Prius"]
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __iter__(self):
        yield from self.cars  # grab each item in the iterable


dealer_cars = Dealership()

car_1 = Car('Rav4', 2005, 'Toyota')
car_2 = Car('Focus', 2020)
car_3 = Car('Focus', 2021)
# Add cars to dealership

# if car_1 == car_2:
if car_3 == car_2:
    print("Equal")
else:
    print("Not equal")

dealer_cars.add_car(car_1)
dealer_cars.add_car(car_2)
dealer_cars.add_car(car_3)

for cars in dealer_cars:
    print(cars)

# print(dir(car_1))
# print(car_1)
# print(str(car_1))

# print(car_1.make)
# print(car_1.stop())
# print(car_1.go(220))
# print(car_1.stop())
# print(car_2.make)
# print(car_2.go("Fast"))
# print(car_2.go("Fast"))
# print(car_2.stop())

# my_car = Car()
# print(type(my_car))
# print(my_car)
# print(isinstance(my_car, Car))

# Car.doors = 5
# car_1.doors = 4
#
# print(f'car_1 {car_1.doors}')
# print(id(car_1.doors))  # id is different thus it doesn't change to 5 doors
# print(f'car_2 {car_2.doors}')
# print(id(car_2.doors))
# print(f'Car {Car.doors}')
# print(id(Car.doors))


