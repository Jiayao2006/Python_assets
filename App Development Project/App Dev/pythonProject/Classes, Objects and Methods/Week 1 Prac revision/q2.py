class Phone:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def get_phone_info(self):
        return f"The price for {self.__make} {self.__model} is ${self.__price}"


make = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")
price = float(input("Enter the price of the phone: "))
phone1 = Phone(make, model, price)
print(phone1.get_phone_info())