class Wallet:
    def __init__ (self, balance):
        self.__balance=balance #For internal use by convention

    def validate(self,amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
    
    def deposit(self, amount):
        self.validate(amount)
        self.__balance += amount #add to the balance safely

    def withdraw(self, amount):
        self.validate(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount #subtract from the balance safely

    def get_balance(self):
        return self.__balance 
# Example usage:    
account1 = Wallet()
account1.deposit(3)
print(account1.get_balance())  # Output: 3

account1.deposit(50)
print(account1.get_balance())  # Output: 53

account1.withdraw(-4)
account1.withdraw(-8)
account1.withdraw(58)  # This will raise an error due to insufficient funds
)