from car import Car


class Truck(Car):
    def __init__(self, module_name, mileage, manufacturer, max_volume):
        super().__init__(module_name, mileage, manufacturer)
        self._max_volume = max_volume
        self._now_volume = 0

    def gas(self):
        if self._now_volume > self._max_volume:
            print("重量オーバーです")
            print(f"最低でも{self._now_volume - self._max_volume}tを降ろしてください")
        else:
            super().gas()

    def load(self, volume):
        if volume > 0:
            print(f"{volume}tの荷物を積みます")
            self._now_volume += volume
            print(self._now_volume)
            if self._now_volume > self._max_volume:
                print("最大積載量を超えています")
        else:
            if self._now_volume < -volume:
                print(f"{-volume}tは降ろせません")
                print(f"{self._now_volume}tの全ての荷物をおろします")
                self._now_volume = 0
                print(self._now_volume)
            else:
                print(f"{-volume}tの荷物を降ろします")
                self._now_volume += volume
                print(self._now_volume)


if __name__ == "__main__":
    truck1 = Truck("xxx", 200, "NISSAN", 100)
    truck1.load(800)
    truck1.load(-10)
    truck1.gas()
