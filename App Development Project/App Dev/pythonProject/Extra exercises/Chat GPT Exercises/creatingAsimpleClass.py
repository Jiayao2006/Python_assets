class Car:
    def __init__(self):
        self.__color = "red"

    def describe(self):
        print(f"The car color is {self.__color}.")


car = Car()
car.describe()