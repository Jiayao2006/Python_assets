class Customer:
    def __init__(self, name, email, mobile_num):
        self.__name = name
        self.__email = email
        self.__mobile_number = mobile_num

    def get_customer_info(self):
        return f"Name: {self.__name}, Email: {self.__email}, Mobile Number: {self.__mobile_number}"

customer1 = Customer("John", "john@nyp.edu.sg", 92345678)
print(customer1.get_customer_info())