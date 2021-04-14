initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_len = len(initial_list)

for list_item in initial_list[:]:
    item_wo_signs = list_item.replace("+", "").replace("-", "")
    if item_wo_signs.isnumeric():
        if ("+" or "-") in list_item:
            list_item = list_item[0] + '{:02}'.format(int(list_item[1:]))
        else:
            list_item = '{:02}'.format(int(list_item))
        initial_list.append('" ')
        initial_list.append(list_item)
        initial_list.append(' "')
    else:
        initial_list.append(list_item)
initial_list = initial_list[list_len:]
print(' '.join(initial_list).replace('"  ', '"').replace('  "', '"'))
