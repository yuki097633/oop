import time


class Account:
    account_number_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.account_number_count
        self.transaction = []
        self.show_account()
        Account.account_number_count += 1

    def withdraw(self, price):
        if self.balance >= price:
            self.balance -= price
            self._write_transaction(-price)
            self.show_account()
        else:
            print(f"残高不足 残高:{self.balance}")

    def deposit(self, price):
        self.balance += price
        self._write_transaction(price)
        self.show_account()

    def show_account(self):
        print(f"口座番号{self.account_number} 口座名:{self.name} 残高:{self.balance}")

    def _write_transaction(self, price):
        transaction = {
            "price": price,
            "balance": self.balance,
            "time": Account._get_time()
        }
        self.transaction.append(transaction)

    def show_transaction(self):
        for tran in self.transaction:
            tran_str_list = []
            for k, v in tran.items():
                tran_str_list.append(f"{k}: {v}")
            print(", ".join(tran_str_list))

    @staticmethod
    def _get_time():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)


account_1 = Account("John", 10000)
account_1.withdraw(1000)
account_1.deposit(3000)
account_1.withdraw(30000)
account_1.show_transaction()

# account_2 = Account("Ema", 10000)
# account_2.withdraw(1000)
# account_2.deposit(3000)
# account_2.withdraw(30000)
#
# account_3 = Account("Michel", 10000)
# account_3.withdraw(1000)
# account_3.deposit(3000)
# account_3.withdraw(30000)
