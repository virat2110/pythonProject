balance = 500000

def withdraw(x):
    global balance
    balance = balance - x
    print(balance)
def deposit(x):
    global balance
    balance = balance + x
    print(balance)
def enquiry():
    global balance
    print(balance)