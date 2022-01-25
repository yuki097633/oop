class Car:
    def __init__(self, module_name, mileage, manufacturer):
        self.module_name = module_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print(f"{self.module_name}")

    def breakes(self):
        print(f"{self.mileage}")


if __name__ == "__main__":
    car1 = Car("Prius", 20, "TOYOTA")
    car1.gas()
