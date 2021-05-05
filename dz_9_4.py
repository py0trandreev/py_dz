class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Поехали!")

    def stop(self):
        print("Стоп машина!")

    def turn(self, direction):
        print(f"Повернули на {direction}")

    def show_speed(self):
        print(f"Едем со скоростью {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Внимание! Разрешенная скорость 60 км/ч. Текущая скорость {self.speed} км/ч")
        else:
            print(f"Едем со скоростью {self.speed} км/час")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Внимание! Разрешенная скорость 40 км/ч. Текущая скорость {self.speed} км/ч")
        else:
            print(f"Едем со скоростью {self.speed} км/ч")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)





car01 = TownCar(50, "зеленый", "Nissan")
car01.show_speed()
car01 = TownCar(80, "зеленый", "Nissan")
car01.show_speed()

print()
car02 = TownCar(80, "синий", "Nissan")
car01.show_speed()

print()
car03 = SportCar(100, "красный", "Феррари")
print(car03.name)

print()
car04 = PoliceCar(40, "белый", "Лада")
print("Это полицейская машина?: ", car04.is_police)
print(car04.name)


