class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self, hight):
        result = self._width * self._length * hight * 25 #пусть - 25 кг весит полотно толщиной 1 см
        return result


r1 = Road(5000, 20)
w1 = r1.get_weight(5)
print(r1._length)
print(r1._width)
print("Вес полотна длиной {} м и шириной {} м составит {:.2f} т".format(r1._length, r1._width, w1/1000))