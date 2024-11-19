Create a banking system that implements different types of bank accounts using inheritance and polymorphism. Your implementation should include the following requirements:

Create a base class BankAccount with:

Private attributes for account number, account holder name, and balance
Methods for deposit and withdrawal
A method to get account information


Create two derived classes:

SavingsAccount that:

Inherits from BankAccount
Has an interest rate attribute
Includes a method to apply interest to the balance
Overrides the get_account_info method to include interest rate


CheckingAccount that:

Inherits from BankAccount
Has an overdraft limit
Overrides the withdrawal method to implement overdraft functionality
Overrides the get_account_info method to include overdraft limit

Requirements:

All attributes should be private
Use proper inheritance and method overriding
Implement appropriate error checking for deposits and withdrawals
Use super() to call parent class methods when appropriate

The system should be able to:

Create different types of accounts
Handle deposits and withdrawals
Display account information
Apply interest to savings accounts
Handle overdrafts for checking accounts

Expected Output:
When run with the test program, your implementation should produce output similar to:

Deposited $500. New balance: $500
Deposited $200. New balance: $700
Withdrew $300. New balance: $1200
Withdrew $600 using overdraft. Balance: $-100
Interest applied: $24.0

Final Account Information:
Account Number: SAV001, Holder: John Doe, Balance: $1224.0, Interest Rate: 2.0%
Account Number: CHK001, Holder: Jane Smith, Balance: $-100, Overdraft Limit: $100