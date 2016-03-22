
'''
bank_account.py
python oop practice
'''

class BankAccount(object):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def show_balance(self):
        return self.balance






if __name__ == '__main__':
    # my_account = BankAccount(1000)
    # print('Your account is just setup. ${}'.format(my_account.show_balance()))
    # print('Deposit: $100. You have ${}'.format(my_account.deposit(100)))
    # print('Withdraw: $500. You have ${}'.format(my_account.withdraw(500)))
