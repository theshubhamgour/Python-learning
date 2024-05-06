# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acccount_number = acc

# debit method
def debit(self,amount):
    self.balance = -amount
    print("Rs.",amount,"was debited")

# debit method
def debit(self,amount):
    self.balance = -amount
    print("Rs.",amount,"was credited")

def get_balance(self):
    return self.balance
    

acc1  = Account(10000,12345)
print(acc1.balance)
print(acc1.acccount_number)