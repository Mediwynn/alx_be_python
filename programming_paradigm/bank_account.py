class BankAccount:
    def __init__(account, account_balance, def_val = 0):
        account.account_balance = account_balance
        account.def_val = def_val
        

    def deposit(amount, account) -> None:
            account.account_balance += amount
            return amount

    def withdraw(amount):
        minus = float(amount)
        if minus >= account.account_balance:
            account.account_balance -= minus
        else:
           return False

    def display_balance():
        current = account.account_balance
        return print(f"Current Balance: ${current}")