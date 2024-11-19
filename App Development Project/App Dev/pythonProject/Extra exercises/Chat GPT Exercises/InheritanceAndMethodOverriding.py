class Vehicle:
    def start_engine(self):
        print("Engine starting")

class Truck(Vehicle):
    def start_engine(self):
        print("Truck engine starting")

vehicle = Vehicle()
vehicle2 = Truck()

vehicle.start_engine()
vehicle2.start_engine()