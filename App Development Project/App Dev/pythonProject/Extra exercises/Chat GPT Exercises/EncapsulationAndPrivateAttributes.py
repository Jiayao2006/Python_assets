class BankAccount:
    def __init__(self, balance_, choice_, amount_):
        self.__balance = balance_
        self.__choice = choice_
        self.__amount = amount_

    def withdraw(self):
        if self.__balance > self.__amount:
            self.__balance = self.__balance - self.__amount
        else:
            print("Insufficient balance for withdrawal!")

    def deposit(self):
        self.__balance = self.__balance + self.__amount
        print(f"${self.__balance} after deposit of ${self.__amount}")


balance = float(input("Enter your balance: "))
choice = input("Deposit or Withdraw: ")
amount = float(input("Enter amount: "))
user1 = BankAccount(balance, choice, amount)

if choice.lower() == "deposit":
    user1.deposit()
elif choice.lower() == "withdraw":
    user1.withdraw()









