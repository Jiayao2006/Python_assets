class SalesPerson:
    def __init__(self):
        self.__name = None
        self.__commission = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def salesperson_commission(self, payment_received):
        commission_percentage = 0.02
        self.__commission = payment_received * commission_percentage

    def __str__(self):
        s = f"The commission of salesperson {self.__name} is ${self.__commission:.2f}"
        return s


input_salesperson_name = input("Enter salesperson name: ")
input_payment_received = float(input("Enter payment received by salesperson: "))
sp = SalesPerson()
sp.set_name(input_salesperson_name)
sp.salesperson_commission(input_payment_received)
print(sp)
