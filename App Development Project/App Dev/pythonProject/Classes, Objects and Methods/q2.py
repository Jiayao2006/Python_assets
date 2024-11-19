class Phone:
    def __init__(self, make, mod, price):
        self.__make = make
        self.__model = mod
        self.__price = price

    def get_phone_info(self):
        return f"The price for {self.__make} {self.__model} is ${self.__price}"

model = Phone(input("Enter the make of the phone: "),
                input("Enter the model of the phone: "),
                int(input("Enter the price of the phone: ")))
print(model.get_phone_info())