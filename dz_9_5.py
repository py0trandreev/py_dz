class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Поставить подпись.")

class Pencil(Stationery):
    def draw(self):
        print("Создать чертеж.")

class Handle(Stationery):
    def draw(self):
        print("Выделить текст.")



stat01 = Pen("Pilot")
print(stat01.title)
stat01.draw()

stat02 = Pencil("Kohi-Noor")
print(stat02.title)
stat02.draw()

stat03 = Handle("Crown")
print(stat03.title)
stat03.draw()

