import random


def of_range(min_words, max_words):
    """ Zwraca tekst o ilości słów z przedziału <min_words, max_words> """
    with open("loremipsum.txt") as file:
        amount = random.randint(min_words, max_words)
        output = ""
        for count, word in enumerate(word_gen(file), start=1):
            if count < amount:
                output += word + " "
            else:
                output += word
                break
        return output


def of_length(words):
    """ Zwraca tekst o ilości słów 'words' """
    with open("loremipsum.txt") as file:
        amount = words
        output = ""
        for count, word in enumerate(word_gen(file), start=1):
            if count < amount:
                output += word + " "
            else:
                output += word
                break
        return output


def word_gen(file):
    """ Generator dla funkcji zwracającej ilość słów - by oszczędzić pamięć przy długich tekstach lub wielu testach """
    for line in file:
        for word in line.split():
            yield word

