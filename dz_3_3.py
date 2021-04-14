import collections

def thesaurus(*args):
    employee_dict = {}

    for name in args:
        employee_ls_as_value = []
        if employee_dict.get(name[0]) is None:
            employee_ls_as_value.append(name)
            employee_dict.setdefault(name[0], employee_ls_as_value)
        else:
            employee_ls_as_existing_value = employee_dict.get(name[0])
            employee_ls_as_existing_value.append(name)
            employee_dict.setdefault(name[0], employee_ls_as_existing_value)

    return collections.OrderedDict(sorted(employee_dict.items()))


print(thesaurus("Геннадий", "Мария", "Александр", "Михаил", "Николай", "Митрофан", "Анна"))
