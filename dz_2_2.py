initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
res_list = []

for list_item in initial_list:
    item_wo_signs = list_item.replace("+", "").replace("-", "")
    if item_wo_signs.isnumeric():
        if ("+" or "-") in list_item:
            list_item = list_item[0] + '{:02}'.format(int(list_item[1:]))
        else:
            list_item = '{:02}'.format(int(list_item))
        res_list.append('" ')
        res_list.append(list_item)
        res_list.append(' "')
    else:
        res_list.append(list_item)

print(' '.join(res_list).replace('"  ','"').replace('  "','"'))


