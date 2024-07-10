class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

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