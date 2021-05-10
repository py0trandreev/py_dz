from abc import ABC, abstractmethod


class Clothes(ABC):
    total_consumption = 0
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self):
        self.__size = 0

    def fabric_consumption(self):
        result = self.size/6.5 + 0.5
        Clothes.total_consumption += result
        return result

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        self.__size = val


class Jacket(Clothes):
    def __init__(self):
        self.__length = 0

    def fabric_consumption(self):
        result = 2*self.length + 0.3
        Clothes.total_consumption += result
        return result

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val):
        self.__length = val

clt1 = Coat()
clt1.size = 34
print(clt1.fabric_consumption())
print(clt1.size)

print(clt1.fabric_consumption())
print("Общий расход ткани {}".format(clt1.total_consumption))


ctl2 = Jacket()
ctl2.length = 60
print(ctl2.fabric_consumption())
print(ctl2.length)
print("Общий расход ткани {}".format(ctl2.total_consumption))

