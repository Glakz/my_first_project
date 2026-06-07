import random


class Wallet:

    def __init__(self, name, currency="USD"):
        self.name = name
        self.currency = currency
        self.balance = 0.0
        self.id = self.generate_id()   

    def generate_id(self):
        id = random.randint(1000000, 9999999)
        return f"{self.name}#{id}"
    
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Balance: {self.balance} {self.currency}"

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            self.balance -= amount
            return f"Balance: {self.balance} {self.currency}"

    def __add__(self, other):
        self.balance += other
        return self

    def __sub__(self, other):
        if self.balance - other < 0:
            return False
        else:
            self.balance -= other
            return self

    def transfer(self, target_account: Wallet, amount):
        if self.balance - amount < 0:
            return False
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            return self
            


    def __str__(self):
        return f"Wallet [{self.id}] | Owner: {self.name} | Balance: {self.balance:.2f} {self.currency}"
    
wallet_sam = Wallet("Sam")
wallet_sam.deposit(300)
wallet_alex = Wallet("Alex")
wallet_alex.deposit(450)

print(wallet_sam)
print(wallet_alex)

wallet_sam.transfer(wallet_alex, 150)

print(wallet_sam)
print(wallet_alex)

wallet_alex.transfer(wallet_sam, 400)

print(wallet_sam)
print(wallet_alex)

