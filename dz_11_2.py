class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


dividend = int(input("Введите делимое (целое число): "))
divisor = int(input("Введите делитель (целое число): "))

try:
    if divisor == 0:
        raise ZeroDivision("Делить на ноль нельзя.")
    else:
        quotient = dividend / divisor
    print("Частное: {}".format(quotient))
except ZeroDivision as err:
    print(err)
