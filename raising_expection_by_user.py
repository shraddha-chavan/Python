def withdraw(balance, amount):
    if amount > balance:
        return ValueError("Insufficient amount in balance")
    return balance - amount
try:
    print(withdraw(100, 150))
except ValueError as e:
    print(e)