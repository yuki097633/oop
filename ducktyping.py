class Duck:
    """
    This a class for Duck.

    Attributes:
        name: Thename of the duck

    Methods
        walk: print *
        quack: print *
        fly: print *
    """

    def __init__(self, name):
        """
        The constructor for Duck class
        :param name:
        """
        self.name = name

    def walk(self):
        print("walking")

    def quack(self):
        print("quack quack")

    def fly(self):
        print("whee")


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking")

    def quack(self):
        print("quack quack")

    def swim(self):
        print("swimming")


def walk_and_quack(duck):
    duck.walk()
    duck.quack()


if __name__ == "__main__":
    print(help(Duck))
    donald = Duck("Donald")
    pingu = Penguin("Pingu")
    donald.walk()
    donald.quack()
    pingu.walk()
    pingu.quack()
    walk_and_quack(donald)
    walk_and_quack(pingu)

