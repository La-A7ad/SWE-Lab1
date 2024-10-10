from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def get_balance(self):
        return float(self._balance)

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def __init__(self, initial_balance=0, interest_rate=0.05):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self._balance * self.interest_rate

    def withdraw(self, amount):
        raise NotImplementedError("Withdrawals are not permitted from SavingsAccount")

class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


savings = SavingsAccount(1000)
savings.deposit(500)
print(savings.get_balance())           
print(savings.calculate_interest())    

checking = CheckingAccount(500)
checking.deposit(200)
checking.withdraw(400)
print(checking.get_balance())           
try:
    checking.withdraw(500)
except ValueError as e:
    print(e)                         


savings = SavingsAccount(1000)
try:
    savings.withdraw(100)
except NotImplementedError as e:
    print(e)                            

# Test Case 4: Invalid Deposit
checking = CheckingAccount(500)
try:
    checking.deposit(-100)
except ValueError as e:
    print(e)                            
