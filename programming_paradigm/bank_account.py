class BankAccount:
    def __init__(self, account_balance, def_val = 0):
        self.account_balance = account_balance
        self.def_val = def_val
        

    def deposit(amount) -> None:
            self.account_balance += amount
            return amount

    def withdraw(amount) -> None:
        minus = float(amount)
        if minus >= self.account_balance:
            self.account_balance -= minus
        else:
           return False

    def display_balance():
        current = self.account_balance
        return print(f"Current Balance: ${current}")