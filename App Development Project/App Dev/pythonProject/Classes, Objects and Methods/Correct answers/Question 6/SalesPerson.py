class SalesPerson:
    def __init__(self):
        self.__name = None
        self.__phone = None
        self.__commission = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def salesperson_commission(self, payment_received):
        commission_percentage = 0.02
        self.__commission = payment_received * commission_percentage

    def salesperson_sold(self, phone):
        self.__phone = phone

    def __str__(self):
        s = (f"Salesperson {self.__name} sold {self.__phone.get_make()} {self.__phone.get_model()} "
             f"at ${self.__phone.get_price()} and earned a commission of ${self.__commission:.2f}.")
        return s
