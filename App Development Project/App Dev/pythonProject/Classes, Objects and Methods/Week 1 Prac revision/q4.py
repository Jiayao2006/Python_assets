class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price.isdigit():
            self.__price = price
        else:
            print("Price should be in numbers.")

    def get_phone_info(self):
        return f"The price of {self.__make} {self.__model} is ${self.__price}"


phone1 = Phone()
make = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")
price = input("Enter the price of the phone: ")

phone1.set_make(make)
phone1.set_model(model)
phone1.set_price(price)
print(phone1.get_phone_info())
