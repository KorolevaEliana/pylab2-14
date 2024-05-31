# 10.1)	Имеется файл JSON с информацией о продуктах: инфа. Напишите программу, которая считывает информацию из этого файла и выводит ее на экран в виде:
# Название: Шоколад
# Цена: 50
# Вес: 100
# В наличии
#
# Название: Кофе
# Цена: 100
# Вес: 250
# Нет в наличии!
#
# Название: Чай
# Цена: 70
# Вес: 50
# # В наличии

import json

name = "products.json"
with open(name, "r", encoding="utf-8") as file:
    data = json.load(file)
    for product in data['products']:
        print(f"Название: {product['name']}" f"\nЦена: {product['price']}" + f"\nВес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("нет в наличии")

# # 10.2)	Модифицируйте программу 10.1 – добавьте в нее код, который добавляет данные в файл JSON (спрашивает их у пользователя)
# # и потом также выводить содержимое итогового файла на экран.
# import json
#
jjjson = "products.json"
def add_item():
    name = input("название товара  ").capitalize()
    price = int(input("стоимость товара "))
    available = input("в наличии ли товар? ").upper()
    if (available == "ДА") or (available == "YES") or (available == "LF"):
        available = True
    else:
        available = False
    weight = int(input("граммовка товара "))
    with open(jjjson, "r", encoding="utf=8") as file:
        data = json.load(file)
        data['products'].append({
            "name": name,
            "price": price,
            "weight": weight,
            "available": available
        })
    with open (jjjson, "w", encoding="utf=8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
add_item()
def showing_list():
    with open(jjjson, "r", encoding="utf=8") as file:
        data = json.load(file)
        for product in data['products']:
                print(f"\nНазвание: {product['name']}" f"\nЦена: {product['price']}" + f"\nВес: {product['weight']}")
                if product['available']:
                    print("В наличии")
                else:
                    print("нет в наличии")
showing_list()
ask1 = int(input("сколько ещё товаров вы хотите добавить?"))
if ask1 >= 0:
    for i in range(ask1):
        add_item()
        showing_list()


# # 10.3)	Создание русско-английского словаря. Имеется файл en-ru.txt, в котором находятся строки	англо-русского словаря в таком формате:
# # cat - кошка
# # dog - собака
# # home - домашняя папка, дом
# # mouse - мышь, манипулятор мышь
# # to do - делать, изготавливать
# # to make – изготавливать
# # и т.п.
# # Требуется создать русско-английский словарь и вывести его в файл ru-en.txt в таком формате:
# # делать – to do
# # дом – home
# # домашняя папка – home catalog
# # изготавливать – to do, to make
# # кошка – cat
# # манипулятор мышь – mouse
# # мышь – mouse
# # собака – dog
# # Обратите	внимание, что строки в выходном файле нужно отсортировать по алфавиту!

from googletrans import Translator
name = "en-ru.txt"
translations_dict = {}
with open(name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
                russian_word, english_word = line.strip().split(" – ")
                translations_dict[russian_word] = english_word

sorted_translations = {}
for [russian_word, english_word] in translations_dict.items():
    sorted_translations[russian_word] = ", ".join(english_word.split(", "))

with open("en-ru_sorted.txt", "w", encoding="utf-8") as file:
        for russian_word, english_word in (sorted_translations.items()):
                file.write(f"{english_word} - {russian_word}\n")
        ask1 = input("вы хотите добавить элемент к словарю? ").upper()
        if (ask1 == "ДА") or (ask1 == "YES") or (ask1 == "LF"):
                def newwords():
                        ask2 = input(
                                "введите 'ENG' если хотите произвести перевод с английского на русский.\nвведите 'RUS' если хотите произвести перевод с русского на английский\n").upper()
                        if ask2 == "ENG":
                                text = (input("какое слово вы хотите перевести(ВЫБРАНО АНГЛ-РУ) "))
                                translator = Translator()
                                result = (translator.translate(text, dest='ru').text)
                                file.write(f"{result} - {text}\n")
                        if ask2 == "RUS":
                                text = (input("какое слово вы хотите перевести(ВЫБРАНО РУ-АНГЛ) "))
                                translator = Translator()
                                result = (translator.translate(text, dest='en').text)
                                file.write(f"{text} - {result}\n")
                        ask3 = input("хотите перевести ещё одно слово? ").upper()
                        if (ask3 == "ДА") or (ask3 == "YES") or (ask3 == "LF"):
                                newwords()
                newwords()
with open("en-ru_sorted.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines.sort()
with open("en-ru_sorted.txt", "w", encoding="utf-8") as file:
        for line in lines:
                file.write(line)