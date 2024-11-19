class BankAccount:
    def __init__(self, acc_num, name, balance):
        self.__acc_num = acc_num
        self.__name = name
        self.__balance = balance

    def get_acc_num(self):
        return self.__acc_num

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def set_acc_num(self, acc_num):
        self.__acc_num = acc_num

    def set_name(self, name):
        self.__name = name

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_account_info(self):
        return (f"Account Number: {self.get_acc_num()}\nAccount Holder Name: {self.get_name()}\n"
                f"Balance: {self.get_balance()}\n")


class SavingsAccount(BankAccount):
    def __init__(self, acc_num, name, balance, interest=0.02):
        super().__init__(acc_num, name, balance)
        self.__interest_rate = interest

    def interest_applied(self):
        interest = self.get_balance() * self.__interest_rate
        return f"Interest amount: {interest}"

    def display_account_info(self):
        return super().display_account_info() + f"Interest Rate: {self.__interest_rate * 100}%"


class CheckingAccount(BankAccount):
    pass