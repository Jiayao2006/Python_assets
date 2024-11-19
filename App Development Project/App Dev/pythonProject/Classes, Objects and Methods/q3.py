class Customer:
    def __init__(self): # initializing function
        self.__name = None
        self.__email = None
        self.__mobile_number = None

    def set_name(self, n): # mutator
        self.__name = n

    def set_email(self, e):
        self.__email = e

    def set_mobile_number(self, mb):
        self.__mobile_number = mb

    def get_name(self): # accessor
        return self.__name

    def get_email(self):
        return self.__email

    def get_mobile_number(self):
        return self.__mobile_number


customer_1 = Customer() # create an object

customer_1.set_name(input("Enter your name: "))
customer_1.set_email(input("Enter your email: "))
customer_1.set_mobile_number(int(input("Enter your mobile number: ")))

print(f"Name: {customer_1.get_name()}\nEmail: {customer_1.get_email()}\nMobile Number: {customer_1.get_mobile_number()} ")
