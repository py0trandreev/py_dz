import random

def get_jokes(joke_count):
    """ Получает заданное в параметре количество шуток из
    заданных 3-х списков слов

        Parameters
        ----------
        joke_count : int
        """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes_ls = []

    for i in range(joke_count):
        rndm_noun = random.choice(nouns)
        rndm_adverb = random.choice(adverbs)
        rndm_adjective = random.choice(adjectives)

        jokes_ls.append("{} {} {}".format(rndm_noun, rndm_adverb, rndm_adjective))

    print(jokes_ls)

get_jokes(10)