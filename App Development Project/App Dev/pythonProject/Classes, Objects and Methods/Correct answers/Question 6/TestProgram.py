from Phone import *
from SalesPerson import *

input_phone_make = input("Enter the make of the phone: ")
input_phone_model = input("Enter the model of the phone: ")
input_phone_price = input("Enter the price of the phone: ")
ph = Phone()
ph.set_make(input_phone_make)
ph.set_model(input_phone_model)
ph.set_price(input_phone_price)
print(ph)
input_salesperson_name = input("Enter salesperson name: ")
input_payment_received = float(input("Enter payment received by salesperson: "))

sp = SalesPerson()
sp.set_name(input_salesperson_name)
sp.salesperson_commission(input_payment_received)
sp.salesperson_sold(ph)
print(sp)
