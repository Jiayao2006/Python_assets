# Question 6
class Phone:
    count = 0  # Class attribute to track the number of Phone objects

    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0
        Phone.count += 1

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if str(price).isnumeric():
            self.__price = float(price)
        else:
            print("Error: Price must be a number.")

    def __str__(self):
        return f"{self.__make} {self.__model} priced at ${self.__price}"

    @staticmethod
    def get_phone_count():
        return Phone.count


class SalesPerson:
    def __init__(self, name=None):
        self.__name = name
        self.__commission = 0
        self.__phone = None  # To store Phone object

    def set_name(self, name):
        self.__name = name

    def salesperson_sold(self, phone):
        self.__phone = phone

    def salesperson_commission(self, payment_received):
        self.__commission = 0.02 * payment_received

    def __str__(self):
        return (f"Salesperson {self.__name} sold {self.__phone} "
                f"and earned a commission of ${self.__commission:.2f}.")


def main():
    # Get phone details from user
    make = input("Enter the make of the phone: ")
    model = input("Enter the model of the phone: ")
    price = input("Enter the price of the phone: ")

    # Create a Phone object and set attributes
    phone = Phone()
    phone.set_make(make)
    phone.set_model(model)
    phone.set_price(price)

    # Display phone creation message
    print(f"The phone created is {phone}. Now has {Phone.get_phone_count()} phone(s) in total.")

    # Get salesperson details from user
    name = input("Enter salesperson name: ")
    payment_received = float(input("Enter payment received by salesperson: "))

    # Create a SalesPerson object
    salesperson = SalesPerson(name)
    salesperson.salesperson_commission(payment_received)

    # Assign the phone to the salesperson
    salesperson.salesperson_sold(phone)

    # Display the salesperson and phone details
    print(salesperson)


# Run the test program
if __name__ == "__main__":
    main()
