class Account:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        if amount >0:
            self.balance+=amount
            print(f"{amount} deposited successfully.new balance is {self.balance}")
        else:
            print("amount should  be greater than zero")

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient funds")
        else:

            self.balance-=amount
            print(f"{amount} withdrawn successfully.new balance is {self.balance}")
    def __str__(self):
        return(f"account_holder: {self.account_holder}\nbalance: {self.balance}")
class savingsaccount(Account):
        def __init__(self,account_holder,balance,interest_rate):
            super().__init__(account_holder,balance)
            self.interest_rate = interest_rate
        def add_interest(self):
            interest = self.balance * self.interest_rate/100
            self.balance+=interest
            print(f"interest added successfully.new balance is {self.balance}")
            def __str__(self):
                return(f"savings account holder:"
            f"{self.account_holder}\nbalance: {self.balance},"
            f"interest rate: {self.interest_rate}")
account = Account('eric',100)
account.deposit(100)
account.withdraw(100)

print(account)

savings=savingsaccount('jane',1000,14)
savings.deposit(500)
savings.withdraw(300)
savings.add_interest()
