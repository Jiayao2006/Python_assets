class Tea:
    def __init__(self, name, origin, colour):
        self.__name = name
        self.__origin = origin
        self.__colour = colour

    def compute_price(self, quantity, unit_price):
        return  quantity * unit_price

    def __str__(self):
        return f"{self.__name} tea from  {self.__origin} has {self.__colour} colour"