import os

ROOT = os.path.dirname(__file__)
DIR = os.path.join(ROOT, 'my_project')
res_dict = {}


def get_category(file_size):
    k = 1
    sizes_list = []
    for el in range(1, 10):
        k = k * 10
        sizes_list.append(k)

    for i in range(len(sizes_list)):
        if i == 0:
            if 0 <= file_size <= sizes_list[i]:
                return sizes_list[i]
        else:
            if sizes_list[i - 1] < file_size <= sizes_list[i]:
                return sizes_list[i]


max_val = []
for root, dirs, files in os.walk(DIR):
    for file in files:
        full_path_to_file = os.path.join(root, file)
        file_size_in_bytes = os.stat(full_path_to_file).st_size
        file_category = get_category(file_size_in_bytes)
        res_dict[file_category] = res_dict.setdefault(file_category, 0) + 1

print(res_dict)
