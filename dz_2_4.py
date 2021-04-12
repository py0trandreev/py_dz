initial_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                'директор аэлита']

for list_item in initial_list:
    last_space = list_item.rfind(" ")
    name = list_item[last_space + 1:]
    name = name[0:1].upper() + name[1:].lower()
    print(f"Привет, {name}!")
