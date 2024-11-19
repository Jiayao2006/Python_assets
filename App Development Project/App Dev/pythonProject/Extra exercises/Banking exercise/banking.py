class BankAccount:
    def __init__(self, account_num, account_holder, balance):
        self.__account_num = account_num
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Incorrect/Insufficient amount')

    def get_account_name(self):
        return self.__account_num

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def set_account_name(self, name):
        self.__account_num = name

    def set_account_holder(self, holder):
        self.__account_holder = holder

    def set_balance(self, balance):
        self.__balance = balance

    def set_account_holder(self, holder):
        self
    def get_account_info(self):
        return f"Name: {self.__account_num}, Holder: {self.__account_holder}, Balance: {self.__balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_num, account_holder, balance, interest=0.02):
        super().__init__(account_num, account_holder, balance)
        self.__interest = interest

    def interest_amount(self):
        return self.__interest * self.get_balance()

    def get_account_info(self):
        return super().get_account_info() + f", Interest Rate: {self.__interest * 100}%, Interest applied: {self.interest_amount()}"

class CheckingAccount(BankAccount):
