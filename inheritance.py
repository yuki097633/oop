class Animal(object):

    def __init__(self, name):
        self.name = name
        print("Animal init is called!!")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)  #継承元のメソッドを呼出
        print("Dog init is called!!")


pochi = Dog("Pochi")

print(pochi.name)
pochi.breath()
