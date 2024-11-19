class Phone:
    count = 0

    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0
        Phone.count += 1

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

    def __str__(self):
        return (f"The phone created is {self.__make} {self.__model} priced at ${self.__price}. "
                f"Now has {Phone.count} phone in total")
