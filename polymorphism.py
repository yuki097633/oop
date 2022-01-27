class Myclass:
    def __str__(self):
        return "Myclassの__str__"

mc = Myclass()
print(mc)  # mc.__str__()
print(1)  # 1.__str__()
print("1")  # "1".__str__()
