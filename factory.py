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


john = Person("John", 20)
print(john.name)

ema = Person.create_from_dob("Ema", 1995, 3, 22)
print(ema.name)
print(ema.age)
