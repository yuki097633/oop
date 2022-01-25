# objectを継承　書かなくてもいい
class Person(object):
    # クラス変数
    num_legs = 2
    count = 0

    # constructor(裏では__new__)
    # インスタンス生成時の初期化メソッド
    def __init__(self, name, age, gender):
        # 変数の定義（引数に与えられた値を）
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking with {Person.num_legs} legs")

    def run(self):
        print(f"{self.name} is running")


john = Person("John", 28, "male")
print(Person.count)
taro = Person("Taro", 18, "male")
print(Person.count)
ema = Person("Ema", 40, "female")
print(Person.count)


# インスタンス変数
print(john.name)
print(john.age)
print(john.gender)

# インスタンスメソッド
john.walk()
ema.walk()
taro.run()

print(john.num_legs)
print(taro.num_legs)

Person.num_legs = 3

print(john.num_legs)
print(taro.num_legs)

# アクセスできるけど非推奨
john.num_legs = 4

print(john.num_legs)
print(taro.num_legs)
