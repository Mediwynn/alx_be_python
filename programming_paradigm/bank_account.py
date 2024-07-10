class BankAccount:
    def __init__(self, name, account_balance, def_bal = 0):
        self.name = name
        self.account_balance = account_balance
        self.def_val = def_val

    def deposit(amount):
        self.account_balance += amount
        added = f"{self.name} deposited: {amount}. current balance is: {self.account_balance}"

    def withdraw(amount):
        if amount >= self.account_balance:
            self.account_balance -= amount
        else:
            print(f"Insufficient funds to withdraw: {amount}")

    def display_balance():
        Current_Balance = self.account_balance
        return print(f"Current balance: ", Current_Balance)