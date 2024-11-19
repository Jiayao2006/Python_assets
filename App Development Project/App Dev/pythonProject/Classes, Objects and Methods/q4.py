class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def set_make(self, m):
        self.__make = m

    def set_model(self, mod):
        self.__model = mod

    def set_price(self, p):
        if p.isdigit():
            self.__price = int(p)
        else:
            print(f"Price should be in numbers.")
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_phone_info(self):
        # Access the attributes of the current instance using self
        return f"The price of {self.get_make()} {self.get_model()} is ${self.get_price()}"

        # return f"The price of {Phone().get_make()} {Phone().get_model()} is ${Phone().get_price()}"
        # Should not create a new Phone object and then calling the getter methods on this new object
        # which results in None values being returned for the make and model and 0 for the price


phone_object = Phone()
phone_object.set_make(input("Enter the make of the phone: "))
phone_object.set_model(input("Enter the model of the phone: "))
phone_object.set_price(input("Enter the price of the phone: "))

print(phone_object.get_phone_info())