class BankAccount:
    def __init__(self, name):
        self._balance = 0
        self.name =name

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
    
    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"Name: {self.name} and Balance: Hidden"
    
# Example 8: Using encapsulation
avipsha = BankAccount("Avipsha")
avipsha.deposit(1000)
print(avipsha)
print(avipsha.get_balance())  # Output: 1000
avipsha.withdraw(500) # output: 500
avipsha.deposit(1000) # output: 1500
avipsha.withdraw(1000) # output: 500
print(avipsha.get_balance())  # Output: 500