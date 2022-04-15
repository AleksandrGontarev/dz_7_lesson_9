############################################   1


def create_list(my_listen: list) -> list:
    """Функция возвращает новый список в котором содержаться элементы из my_list по следующему правилу:
       Если строка стоит на нечетном месте в my_list, то ее заменить на перевернутую строку. "qwe" на "ewq".
       Если на четном - оставить без изменения"""
    new_list = []
    for index, symbol in enumerate(my_listen):
        if index % 2:
            new_list.append(symbol[::-1])
        else:
            new_list.append(symbol)
    return new_list


my_list = ["qwe", "rty", "uio", "asd"]
print(create_list(my_list))

#############################################   2


def get_list_with_forward_symbol_a(in_source: list) -> list:
    """Функция возвращает новый список в котором содержаться элементы
       из my_list у которых первый символ - буква "a"."""
    new_list = []
    for symbol in in_source:
        if symbol[0] == "a":
            new_list.append(symbol)
    return new_list


my_list = ["qwe", "aty", "uio", "asd"]
print(get_list_with_forward_symbol_a(my_list))

###########################################   3


def get_list_with_symbol_a(in_source: list) -> list:
    """Функция возвращает новый список в котором содержаться элементы из my_list
       в которых есть символ - буква "a" на любом месте."""
    new_list = []
    for symbol in in_source:
        if symbol.count("a"):
            new_list.append(symbol)
    return new_list


my_list = ["qwe", "ray", "uio", "asd"]
print(get_list_with_symbol_a(my_list))

#########################################    4


def get_str_from_list(my_listen: list) -> list:
    """Функция возвращает новый список в котором содержаться только строки из my_list."""
    new_list = []
    for symbol in my_listen:
        if type(symbol) == str:
            new_list.append(symbol)
    return new_list


my_list = [1, 2, 3, "11", "22", 33]
print(get_str_from_list(my_list))

#########################################    5


def find_repeat_letters(my_string: str) -> list:
    """Функция возвращает новый список в котором содержаться те символы из my_str,
       которые встречаются в строке только один раз."""
    my_listen = []
    for symbol in set(my_string):
        if my_str.count(symbol) == 1:
            my_listen.append(symbol)
    return my_listen


my_str = "aiiyytttu"
print(find_repeat_letters(my_str))

##############################################    6

def get_new_list_with_repeat_symbol(str_1: str, str_2: str) -> list:
    """Функция возвращает список в который поместить те символы,
       которые есть в обеих строках хотя бы раз."""
    return list(set(str_1).intersection(set(str_2)))


my_str_1 = "akjs"
my_str_2 = "asko"
print(get_new_list_with_repeat_symbol(my_str_1, my_str_2))

############################################    7


def get_new_list_with_repeat_symbol_once(str_1: str, str_2: str) -> list:
    """ Функция возвращает список в который поместить те символы, которые есть в обеих строках,
        но в каждой только по одному разу"""
    res_list = []
    for symbol in set(str_1).intersection((set(str_2))):
        if str_1.count(symbol) == 1 and str_2.count(symbol) == 1:
            res_list.append(symbol)
    return res_list


my_str_1 = "aaadtfr"
my_str_2 = "asdfgh"
print(get_new_list_with_repeat_symbol_once(my_str_1, my_str_2))

#############################################     8

import random
import string


def create_email(name: list, domain: list) -> str:
    """ функция для генерирования e-mail в формате:
        фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен"""
    value_names = random.choice(names)
    value_domains = random.choice(domains)
    value_random_int = random.randint(100, 999)
    value_random_str = ''.join(random.choice(string.ascii_lowercase) for idx in range(0, random.randint(5, 7)))
    return (f"{value_names}.{value_random_int}@{value_random_str}.{value_domains}")


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
email = create_email(names,domains)
print(email)