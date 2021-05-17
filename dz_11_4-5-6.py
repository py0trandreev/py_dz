from abc import ABC, abstractmethod


class Stock:
    def __init__(self):
        self.stock_dict = {}

    def take_in_goods(self, goods_name):
        self.stock_dict[goods_name] = self.stock_dict.setdefault(goods_name, 0) + 1

    def transfer_goods(self, goods_name, other):
        self.stock_dict[goods_name] = self.stock_dict.setdefault(goods_name) - 1
        other.stock_dict[goods_name] = other.stock_dict.setdefault(goods_name, 0) + 1


class Office_equipment(ABC):

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand_name):
        self.__brand = brand_name

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost_value):
        self.__cost = cost_value

    @property
    def paper_size(self):
        return self.__paper_size

    @paper_size.setter
    def paper_size(self, paper_sz):
        self.__paper_size = paper_sz

    def __str__(self):
        return "Марка: {}; размер бумаги: {}; стоимость: {} руб.".format(self.__brand, self.__paper_size, self.__cost)


class Printer(Office_equipment):
    def __init__(self):
        self.__is_colored = False

    @property
    def is_colored(self):
        return self.__is_colored

    @is_colored.setter
    def is_colored(self, colored):
        self.__is_colored = colored

    def __str__(self):
        base_description = Office_equipment.__str__(self)
        return "{} Цветной: {}".format(base_description, self.__is_colored)


class Scanner(Office_equipment):
    def __init__(self):
        self.__scanner_type = "Планшетный"

    @property
    def scanner_type(self):
        return self.__scanner_type

    @scanner_type.setter
    def scanner_type(self, scan_type):
        self.__scanner_type = scan_type

    def __str__(self):
        base_description = Office_equipment.__str__(self)
        return "{} Тип сканера: {}".format(base_description, self.__scanner_type)


class Xerox(Office_equipment):
    def __init__(self):
        self.__cartridge_capacity_in_pages = 0

    @property
    def cartridge_capacity_in_pages(self):
        return self.__cartridge_capacity_in_pages

    @cartridge_capacity_in_pages.setter
    def cartridge_capacity_in_pages(self, cartridge_capacity):
        self.__cartridge_capacity_in_pages = cartridge_capacity

    def __str__(self):
        base_description = Office_equipment.__str__(self)
        return "{} Ресурс картриджа: {}".format(base_description, self.__cartridge_capacity_in_pages)


pr1 = Printer()
pr1.brand = "Epson"
pr1.cost = 15000
pr1.paper_size = "A4"
pr1.is_colored = True
print(pr1.is_colored)
print(pr1)

xer1 = Xerox()
xer1.brand = "Xerox"
xer1.cost = 20000
xer1.paper_size = "A3"
xer1.cartridge_capacity_in_pages = 2000
print(xer1)

office_eq_stock = Stock()
office_eq_stock.take_in_goods(pr1.brand)
office_eq_stock.take_in_goods(pr1.brand)
office_eq_stock.take_in_goods(pr1.brand)
office_eq_stock.take_in_goods(xer1.brand)
office_eq_stock.take_in_goods(xer1.brand)
print(office_eq_stock.stock_dict)

buh_stock = Stock()

office_eq_stock.transfer_goods(pr1.brand, buh_stock)
print(office_eq_stock.stock_dict)
print(buh_stock.stock_dict)
