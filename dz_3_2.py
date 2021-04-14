def num_translate_adv(num_eng_str):
    number_dict = {'zero': 'ноль',
                   'one': 'один',
                   'two': 'два',
                   'three': 'три',
                   'four': 'четыре',
                   'five': 'пять',
                   'six': 'шесть',
                   'seven': 'семь',
                   'eight': 'восемь',
                   'nine': 'девять',
                   'ten': 'десять'}

    is_lower_1st_char = lambda num_eng_str: num_eng_str[0].islower()
    tmp = number_dict.get(num_eng_str.lower())

    if is_lower_1st_char(num_eng_str):
        return tmp
    else:
        return tmp[0].upper() + tmp[1:]



print(num_translate_adv('One'))
print(num_translate_adv('Five'))
print(num_translate_adv('nine'))
print(num_translate_adv('six'))
print(num_translate_adv('eleven'))
