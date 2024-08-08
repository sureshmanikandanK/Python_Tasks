class Transport:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def Display(self):
        return f'{self.brand} and {self.model}'

class Car(Transport):
    pass

class Boat(Transport):
    pass
class Bike(Transport):
    pass

Four_wheel = Car('Ford', '2024')
print(Four_wheel.Display())
Boat_ship = Car('Titanic', '2024')
print(Boat_ship.Display())
Two_wheel = Bike('Pulsar', '2024')
print(Two_wheel.Display())

