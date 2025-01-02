class NoMoneyException(Exception):
    pass

class OutOfBudget(Exception):
    pass

balance = int(input("Enter a balance to withdraw: "))
try:
    if balance < 1000:
        raise NoMoneyException("You have no money to withdraw")
    elif balance > 10000:
        raise OutOfBudget("You have reached yout limit")
except Exception as error:
    print(error)