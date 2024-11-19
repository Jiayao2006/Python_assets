class Phone:
    count = 0

    def __init__(self):
        self.__id = None
        self.__make = None
        self.__model = None
        self.__price = 0
        self.__class__.count += 1

    def set_id(self, phone_id):
        self.__id = phone_id

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price.isnumeric():
            self.__price = price
        else:
            print("Price should be in numbers.")

    def get_id(self):
        return self.__id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        s = (f"The phone created is {self.__make} {self.__model} priced at ${self.__price}. "
             f"Now has {self.__class__.count} phone in total")
        return s

