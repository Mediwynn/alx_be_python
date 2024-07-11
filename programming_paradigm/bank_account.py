class BankAccount:
    def __init__(self, account_balance, def_val = 100):
        self.account_balance = account_balance
        self.def_val = def_val
        

    def deposit(self, amount) -> None:
            self.account_balance += amount
            return amount

    def withdraw(self, amount) -> None:
        if amount > self.account_balance:
            self.account_balance -= amount
        else:
           return False

    def display_balance(self):
        current = float(self.account_balance)
        disp = print(f"Current Balance: ${current:.2f}")
        return disp