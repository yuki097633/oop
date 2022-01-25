class MyClass:

    classmethod_count = 0

    def mymethod(self):
        print("This is normal method {}".format(self))

    @staticmethod
    def mystaticmethod():
        print("This is static method")

    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print("This is class method {}".format(cls.classmethod_count))


# c = MyClass()
# c.mymethod()

MyClass.myclassmethod()
MyClass.myclassmethod()
