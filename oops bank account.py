# Base class: BankAccount
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance


# Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * self.interest_rate


# Subclass: CurrentAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.minimum_balance:
            super().withdraw(amount)
        else:
            print("Withdrawal would violate minimum balance requirement.")

savings = SavingsAccount(101, 1000, 0.05)
current = CurrentAccount(102, 500, 100)

savings.deposit(500)
print(f"Savings Balance: {savings.get_balance()}")
print(f"Interest Earned: {savings.calculate_interest()}")

current.withdraw(200)
print(f"Current Balance: {current.get_balance()}")
current.withdraw(400)