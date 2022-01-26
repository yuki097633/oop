import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return cls(name=name, age=age)

    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return Person(name=name, age=age)


class Baby(Person):
    pass


john = Baby("John", 20)
print(john.name, john.age)

ema = Baby.create_from_dob("Ema", 1995, 3, 22)
print(ema.name, ema.age)

emily = Baby.create_from_dob2("Emily", 1994, 10, 22)
print(emily.name, emily.age)

print(type(john))
print(type(ema))  # 継承先のクラスなのでBabyになる
print(type(emily))  # 継承元のクラスなのでPersonになる バグの元になる
