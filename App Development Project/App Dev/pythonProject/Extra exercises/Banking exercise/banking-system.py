# Create a banking system with the following specifications:
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        print("withdraw:" + str(amount))
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        print("Insufficient funds or invalid withdrawal amount")
        return "Insufficient funds or invalid withdrawal amount"
    
    def get_balance(self):
        return self.__balance
    
    def get_account_info(self):
        return f"Account Number: {self.__account_number}, Holder: {self.__account_holder}, Balance: ${self.__balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        return f"Interest applied: ${interest}"
    
    def get_account_info(self):
        return super().get_account_info() + f", Interest Rate: {self.__interest_rate*100}%"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.__overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        print("withdraw:" + str(amount))
        if amount > 0 and self.get_balance() + self.__overdraft_limit >= amount:
            if self.get_balance() >= amount:
                return super().withdraw(amount)
            else:
                actual_balance = self.get_balance()
                super().withdraw(actual_balance)
                remaining = amount - actual_balance
                print("remaining:" + str(remaining))
                #super().withdraw(remaining)
                self.__overdraft_limit = self.__overdraft_limit - remaining
                return f"Withdrew ${remaining} using overdraft. Balance: ${self.get_balance()}"
        return "Amount exceeds overdraft limit or invalid withdrawal amount"
    
    def get_account_info(self):
        return super().get_account_info() + f", Overdraft Limit: ${self.__overdraft_limit}"

# Test program
def test_bank_accounts():
    # Create accounts
    savings = SavingsAccount("SAV001", "John Doe", 0)
    checking = CheckingAccount("CHK001", "Jane Smith", 0)
    
    # Test deposits
    print(savings.deposit(500))
    print(checking.deposit(200))
    
    # Test withdrawals
    print(savings.withdraw(300))
    print(checking.withdraw(250))  # Should use overdraft
    
    # Test interest application
    print(savings.apply_interest())
    
    # Print account information
    print("\nFinal Account Information:")
    print(savings.get_account_info())
    print(checking.get_account_info())

if __name__ == "__main__":
    test_bank_accounts()
