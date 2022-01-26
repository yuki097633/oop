class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, price):
        self.__balance += price
        self.show_balance()

    def withdraw(self, price):
        if self.__balance < price:
            print("残高が足りません")
        else:
            self.__balance -= price
            self.show_balance()

    def show_balance(self):
        print(f"残高は{self.__balance}円")


myaccount = Account(10000)
print(dir(myaccount))

myaccount.deposit(1000)
myaccount.withdraw(2000)

myaccount.__balance = -1000  # "_"でも更新できちゃうけどね
print(myaccount.__balance)  #__balance属性が出来てしまう
print(dir(myaccount))

myaccount.deposit(1000)
