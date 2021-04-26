import json
import sys

USERS = "users.csv"
HOBBIES = 'hobby.csv'
USER_HOBBY_LIST = 'user_hobby_list.json'


def users_hobbies_iter(users_ls, hobbies_ls):
    # delete \n elements in the end of a list
    def del_newline_elements(ls_to_lookthrough):
        for el in range(len(ls_to_lookthrough) - 1, 0, -1):
            if ls_to_lookthrough[el] == '\n':
                ls_to_lookthrough.pop()
            else:
                break

    del_newline_elements(users_ls)
    del_newline_elements(hobbies_ls)

    # exit with 1
    if len(hobbies_ls) > len(users_ls):
        print("Hobbies is more than users!")
        sys.exit(1)

    for el_user_ind in range(len(users_ls)):
        if el_user_ind < len(hobbies_ls):
            user = users_ls[el_user_ind]
            hobby = hobbies_ls[el_user_ind]
        else:
            user = users_ls[el_user_ind]
            hobby = None
        yield user, hobby


user_hobby_dict = {}
with open(USERS, 'r', encoding="utf-8") as f1, \
        open(HOBBIES, 'r', encoding="utf-8") as f2, \
        open(USER_HOBBY_LIST, 'w', encoding="utf-8") as f3:

    user_lines_ls = f1.readlines()
    hobby_lines_ls = f2.readlines()

    for user2, hobby2 in users_hobbies_iter(user_lines_ls, hobby_lines_ls):
        user_hobby_dict.setdefault(user2.rstrip(), hobby2 if not hobby2 else hobby2.rstrip())

    json.dump(user_hobby_dict, f3)


print(user_hobby_dict)
