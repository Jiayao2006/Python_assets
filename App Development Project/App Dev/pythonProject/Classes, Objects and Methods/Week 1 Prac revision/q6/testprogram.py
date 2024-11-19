from SalesPerson import SalesPerson
from phone import Phone


def main():
    phone1 = Phone()  # when object is created, count will add 1
    make = input("Enter the make of the phone: ")
    model = input("Enter the model of the phone: ")
    price = input("Enter the price of the phone: ")

    phone1.set_price(price)
    phone1.set_make(make)
    phone1.set_model(model)
    print(phone1.__str__())

    salesperson = SalesPerson()
    name = input("Enter salesperson name: ")
    payment = float(input("Enter payment received by salesperson: "))
    salesperson.set_name(name)
    salesperson.salesperson_commission(payment)
    salesperson.salesperson_sold(phone1)
    print(salesperson.__str__())


if __name__ == "__main__":
    main()
