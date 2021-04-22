tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Игорь'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def tut_classes(tutors_ls, klasses_ls):
    tutor = None
    klass = None
    for el_tutor in range(len(tutors_ls)):
        if el_tutor < len(klasses_ls):
            tutor = tutors_ls[el_tutor]
            klass = klasses_ls[el_tutor]

        else:
            tutor = tutors_ls[el_tutor]
            klass = None
        yield tutor, klass


tut_class = tut_classes(tutors, klasses)
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))
print(next(tut_class))

