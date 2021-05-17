import math


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, date_input: str):
        date_ls = date_input.split("-")
        day, month, year = date_ls
        if Date.is_date_correct(int(day), int(month), int(year)):
            return cls(int(day), int(month), int(year))

    @staticmethod
    def is_date_correct(day: int, month: int, year: int):
        try:
            if not 1900 <= year <= 3000:
                raise Exception("Год должен находиться в промежутке от 1900 до 3000")

            if not 1 <= month <= 12:
                raise Exception("Месяц должен находиться от 1 до 12")

            if not 1 <= day <= 28:
                if day < 1:
                    raise Exception("День не может быть меньше 1")

                if month == 2:
                    if round(math.sin(year * math.pi / 4), 1) == 0:
                        # високосный год
                        if day > 29:
                            raise Exception("День не может быть больше 29")
                    else:
                        if day > 28:
                            raise Exception("День не может быть больше 28")

                elif 1 <= month <= 7:
                    if month in range(1, 8, 2):
                        if day > 31:
                            raise Exception("День не должен превышать 31")
                    else:
                        if day > 30:
                            raise Exception("День не должен превышать 30")

                else:
                    if month in range(8, 13, 2):
                        if day > 31:
                            raise Exception("День не должен превышать 31")

                    else:
                        if day > 30:
                            raise Exception("День не должен превышать 30")
            return True
        except Exception as e:
            print(e)
            return False


print(Date.is_date_correct(29, 2, 2021))

date1 = Date.set_date("29-02-2020")
print("Год {}".format(date1.year))
print("Месяц {}".format(date1.month))
print("День {}".format(date1.day))
