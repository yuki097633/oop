class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age  #setterやgetter変数は"_"をつけること

    def set_age(self, age):
        print("set age called!!!!")
        if age < 0:
            print("0以上の値を入れてください")
        else:
            self._age = age

    def get_age(self):
        print("get age called!!!!")
        return self._age

    # バリデーションをsetterに書いておいてpropertyに渡すような使い方をする
    age = property(get_age, set_age)


john = Person("John", 20)
print(john.age)
john.age = -10
