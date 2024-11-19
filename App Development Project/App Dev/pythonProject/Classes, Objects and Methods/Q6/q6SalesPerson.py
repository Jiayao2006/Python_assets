# salesperson.py

class SalesPerson:
    def __init__(self):
        self.__name = None
        self.__commission = 0
        self.__phone = None  # To store the phone object sold

    def set_name(self, n):
        self.__name = n

    def get_name(self):
        return self.__name

    def salesperson_commission(self, payment):
        self.__commission = 0.02 * payment

    def salesperson_sold(self, phone):
        self.__phone = phone  # Store the phone object sold

    def __str__(self):
        return (f"Salesperson {self.get_name()} sold {self.__phone.get_make()} "
                f"{self.__phone.get_model()} at ${self.__phone.get_price()} and earned "
                f"a commission of ${self.__commission:.2f}.")
