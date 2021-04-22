src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

src_dict = {}
for el in src:
    src_dict[el] = src_dict.setdefault(el, 0) + 1

result = [el_key for el_key in src_dict if src_dict[el_key] == 1]


print(result)


