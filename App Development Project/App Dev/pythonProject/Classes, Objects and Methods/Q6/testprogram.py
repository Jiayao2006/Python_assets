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
    print(f"Now has {Phone.get_phone_count()} phone(s) in total.\n")

    # Create and setup SalesPerson object
    salesperson = SalesPerson()
    salesperson.set_name(input("Enter salesperson name: "))
    salesperson.salesperson_commission(int(input("Enter payment received by salesperson: ")))

    # Assign the phone to the salesperson
    salesperson.salesperson_sold(phone)

    # Display salesperson information
    print(salesperson)


# Run the test program
if __name__ == "__main__":
    main()
