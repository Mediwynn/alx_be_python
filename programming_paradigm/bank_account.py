class BankAccount:
    def __init__(self, account_balance, def_val = 0):
        self.account_balance = account_balance
        self.def_val = def_val

    def isnum(amount):
        try:
            num = float(amount)
        except ValueError:
            print(f"Not a valid number provided")
        else:
            return True
        

    def deposit(amount):
        if isnum(amount) == True:
            self.account_balance += amount
            added = f"{self.name} deposited: {amount}. current balance is: {self.account_balance}"
            return added
        else:
            print("Retry number input")

    def withdraw(amount):
        minus = float(amount)
        if minus >= self.account_balance:
            self.account_balance -= minus
        else:
            print(f"Insufficient funds to withdraw: {amount}")


    def display_balance():
        Current_Balance = self.account_balance
        return print(f"Current balance:", Current_Balance)