#6.1) Создайте словарь, содержащий перечень стран и их столиц.
# a) Выведите на экран все пары ключ-значение.
# b) Выведите на экран столицу для определенной страны.
# c) Отсортируйте и выведите на экран содержимое словаря в алфавитном порядке названий стран.
def first():
    capitals = {
        "Russia": "Moscow",
        "German": "Berlin",
        "India": "New Delhi",
        "Switzerland": "Bern",
        "France": "Pariz",
        "Poland": "Warsaw",
        "Netherlands": "Amsterdam",
        "Kazakhstan": "Astana",
        "Australia": "Canberra",
        "Spain": "Madrid"
    }
    country = input("type the country ")
    country = country.capitalize()
    if country in capitals:
        print("capital:", capitals[country])
    else:
        print("none")
    for key, value in capitals.items():
        print(f"{key}: {value}")
    print("sorted dict:", dict(sorted(capitals.items())))
    
#6.2) В игре в слова «Эрудит» каждая буква имеет определенную ценность:
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
def erudittt():
    import re
    erudit = {
        'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1',
        'Д': '2', 'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2',
        'Б': "3", 'Е': "3", 'Ё': "3", 'Ь': "3", 'Я': "3",
        'Й': '4', 'Ы': "4",
        'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5',
        'Ш': '8', 'Э': '8', 'Ю': '8',
        'Ф': '10', 'Щ': '10', 'Ъ': '10'
    }
    play = input("enter the word ").upper()
    for i in play:
        if i not in erudit:
            exit()
    for i in erudit:
        play = re.sub(i, erudit[i], play)
    print(sum(map(int, play)))

#6.3) *Доп.задание на множество.
# Есть множество студентов. Каждый из них знает некоторое количество языков.
# а) Нужно определить сколько различных языков знают студенты.
# б) Выведите отсортированный список этих языков.
# в) Выведите список студентов, которые знают китайский язык.
def dop1():
    students = {
        "name1": ["english", "spanish", "chinese"],
        "name2": ["french", "german", "chinese"],
        "name3": ["italian", "english"],
        "name4": ["english", "german", "hindi"],
        "name5": ["chinese", "arabic", "turkish"]
    }
    lang = set()
    for i in students:
        lang.update(students[i])
        num_lang = len(lang)
    print(f"number of languages students can speak: {num_lang}")

    sorted_languages = sorted(list(lang))
    print("sorted languages:", sorted_languages, "\namount of students who can speak chinese:")

    ch = [i for i in students if "chinese" in students[i]]
    for y in ch:
        print(y)

def dop2():
    import random
    languages = ['arabic', 'chinese', 'english', 'french', 'german', 'hindi', 'italian', 'spanish', 'turkish']
    students = {}
    studentamount = random.randint(2,11)
    for i in range(1,studentamount):
        num_languages = random.randint(1,5)
        student_languages = random.sample(languages, num_languages)
        students["student" + str(i)] = student_languages
    lang = set()
    for i in students:
        lang.update(students[i])
        num_lang = len(lang)
    print(f"number of languages students can speak: {num_lang}")
    sorted_languages = sorted(list(lang))
    print("sorted languages:", sorted_languages, "\namount of students who can speak chinese:")

    ch = [i for i in students if "chinese" in students[i]]
    for y in ch:
        print(y)
# first(), erudittt(), dop(), dop2()