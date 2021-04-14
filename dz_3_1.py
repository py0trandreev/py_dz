def num_translate(num_eng_str):
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
    return number_dict.get(num_eng_str)


print(num_translate('one'))
print(num_translate('five'))
print(num_translate('eleven'))
