class NoNumericListItemsError(Exception):
    """Возникает, если при поытке добавить не числовое значение в список

    Attributes:
        message -- пояснение ошибки
    """

    def __init__(self, message="Значение не является числом"):
        self.message = message


input_list = []

while True:
    user_value = input("Введите число для добавления в список: ")

    if user_value == 'stop':
        print("Выход из программы...")
        print(input_list)
        break

    try:
        user_value_as_number = float(user_value)
        if "." not in user_value:
            user_value_as_number = int(user_value)

        input_list.append(user_value_as_number)
    except ValueError as err:
        try:
            raise NoNumericListItemsError("Введено не число!")
        except NoNumericListItemsError as err:
            print(err)
