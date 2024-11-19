# phone.py

class Phone:
    count = 0  # Class attribute to track the number of Phone objects created

    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0
        Phone.count += 1  # Increment the count every time a Phone object is created
        self.__id  = None

    def set_id(self, id):
        self.__id = id

    def set_make(self, m):
        self.__make = m

    def set_model(self, mod):
        self.__model = mod

    def set_price(self, p):
        if p.isdigit():
            self.__price = int(p)
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
        return f"The phone created is {self.get_make()} {self.get_model()} priced at ${self.get_price()}."

    @staticmethod
    def get_phone_count():
        return Phone.count  # Return the total number of Phone objects created
