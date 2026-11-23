class InsufficientFundsError(ValueError):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )

        self.balance -= amount
        self.history.append(("withdraw", amount))

    def statement(self):
        lines = [f"Statement for {self.owner}"]
        lines.extend(
            f"{kind:<10}{amount:>8}" for kind, amount in self.history
        )
        lines.append(f"Balance: {self.balance}")
        return "\n".join(lines)


acc = BankAccount("Maria")
acc.deposit(200)
acc.withdraw(75)
try:
    acc.withdraw(500)
except InsufficientFundsError as err:
    print("Error:", err)
try:
    acc.deposit(-5)
except ValueError as err:
    print("Error:", err)
print(acc.statement())