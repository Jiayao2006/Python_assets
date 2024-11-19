class SalesPerson:
    def __init__(self):
        self.__name = None
        self.__commission = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def salesperson_commission(self, payment_received):
        self.__commission = 0.02 * payment_received

    def __str__(self):
        return f"The commission of salesperson {self.__name} is ${self.__commission:.2f}"


salesperson = SalesPerson()

name = input("Enter salesperson name: ")
payment = int(input("Enter payment received by salesperson: "))

salesperson.set_name(name)
salesperson.salesperson_commission(payment)
print(salesperson.__str__())
