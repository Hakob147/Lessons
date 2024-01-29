class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
    def get_balance(self):
        return self.balance

client_1 = BankAccount("account1", 1000)
client_1.deposit(500)
client_1.withdraw(200)
print(client_1.get_balance())

