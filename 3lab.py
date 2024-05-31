# 3.1)	С клавиатуры вводятся поочередно N слов. Напишите программу, которая соединяет эти слова в одну длинную строку,
# разделяя слова пробелами. Используйте операторы цикла.
def fff():
    num = int(input("skolko slov v programme "))
    res = " ".join(input("vvedite slovo ") for i in range(num))
    print(res)

# 3.2)	Модифицируйте предыдущую программу так, чтобы число вводимых слов не было задано,
# а программа работала до того момента, как пользователь введет слово «stop».
def seccond():
    words = []
    while True:
        word = input("vvedite slovo ")
        if word == 'stop':
            break
        words.append(word)
    result = ' '.join(words)
    print(result)

# 3.3)	В игре в слова ценится наличие редких букв в словах.
# Считается, что буква "ф" встречается в русском языке реже всех остальных. Напишите программу,
# которая позволяет пользователям вводить какие-либо слова и проверяет, можно считать это слово редким или нет.
# Редкими будем считать слова, которые содержат букву "ф". Пусть эта программа выводит на экран одну из двух фраз: "Ого! Это редкое слово!",
# если в слове есть буква "ф", или "Эх, это не очень редкое слово...", если в нём этой буквы нет.
def third():
    import re
    word = input("vvedite ochen redkoye slovo ")
    match = re.search(r'[Ff]', word)
    if match:
        print("wow! eto redkoye slovo!")
    else:
        print("uh, eto ne ochen redkoye slovo...")
def third2():
    word = input("vvedite ochen redkoye slovo ")
    for i in range(len(word)):
        if (word[i] == "f" or word[i] == "F"):
            print("wow! eto redkoye slovo!")
            exit()
    else:
        print("uh, eto ne ochen redkoye slovo...")

# 3.4) Напишите программу-игру «Математика для детей»: компьютер выводит выражение-сумму двух чисел, например: 3 + 5 =
# Пользователь должен ввести ответ (курсор должен оставаться в одной строке с заданным выражением). Если ответ правильный,
# то вывести сообщение после результата «Правильно!», если ответ неправильный, то вывести сообщение «Ответ неверный».
# Игра продолжается в цикле до тех пор, пока пользователь не сделает 3 ошибки.
# После этого вывести сообщение: «Игра окончена. Правильных ответов: …» - вместо многоточия вывести количество правильных ответов.
def math():
    import random
    mistakes = 0
    points = 0
    while mistakes < 3:
        num1 = random.randint(1, 999)
        num2 = random.randint(1, 999)
        correct = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))
        if user_answer == correct:
            print("pravilno!")
            points += 1
        else:
            print("otvet neverny")
            mistakes += 1
    print("igra oconchena. Pravilnih otvetov:", points)

fff(), seccond(), third(), third2(), math()