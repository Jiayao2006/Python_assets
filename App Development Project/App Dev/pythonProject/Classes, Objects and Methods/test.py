# test_program.py

from q6Phone import Phone
from q6SalesPerson import SalesPerson


def main():
    # Create and setup Phone object
    phone = Phone()
    phone.set_make(input("Enter the make of the phone: "))
    phone.set_model(input("Enter the model of the phone: "))
    phone.set_price(input("Enter the price of the phone: "))

    # Display phone information
    print(phone.get_phone_info())

    # Create and setup SalesPerson object
    salesperson = SalesPerson()
    salesperson.set_name(input("Enter salesperson name: "))
    salesperson.salesperson_commission(int(input("Enter the payment amount: ")))

    # Display salesperson information
    print(salesperson)


# Run the test program
if __name__ == "__main__":
    main()
