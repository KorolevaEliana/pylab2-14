# 5.1) Создайте список из пяти любых чисел. Спросите у пользователя число. Проверьте, есть ли данное число в списке.
# Выведите исходный список, число пользователя и соответствующие сообщение ("Поздравляю, Вы угадали число!" или "Нет такого числа!").
def first():
    numbers = [12,32,567,26,7]
    print(int(input("try to guess the number ")) in numbers)

# 5.2)Создайте любой список. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение.
def seccond():
    list = ["sesese", "lelele", "nununu", "momomo", "sesese", "kikiki", "kikiki"]
    addition = {}
    for i in list:
        if i in addition:
            addition[i] += 1
        else:
            addition[i] = 1
    for item, v in addition.items():
        if v > 1:
            print(f"repeating element: {item}")
#5.3) Задан кортеж с перечнем названий дней недели. Спросить у пользователя, сколько выходных на неделе он хочет и вывести два списка:
# "Ваши выходные дни: ..." - перечислить здесь столько дней недели с конца кортежа, сколько введено пользователем.
# "Ваши рабочие дни: ..." - перечислить здесь оставшиеся дни недели.
def third():
    days = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
    ask = int(input("how many weekends do you want? "))
    if (ask >= 8 or ask <= -1):
        exit()
    weekend = days[-ask:]
    work = days[:-ask]
    if ask == 0:
        lst_we = ("none")
        lst_work = ", ".join(days)
    elif ask == 7:
        lst_we = ", ".join(weekend)
        lst_work = ("none")
    else:
        lst_we = ", ".join(weekend)
        lst_work = ", ".join(work)
    print("weekends:", lst_we, "\nwork:", lst_work)

# 5.4) Создайте два списка: один из 10 фамилий студентов Вашей группы, другой из 10 фамилий студентов другой группы.
# a. Создайте спортивную команду (объедините в один кортеж) по 5 любых студентов из каждой группы.
# b. Выведите на экран исходные списки групп и новый полученный кортеж.
# c. Выведите его длину.
# d. Отсортируйте кортеж по алфавиту.
# e. Определите, входит ли в полученную команду студент "Иванов". И сколько раз встречается эта фамилия в кортеже.
import random
group1 = ["surn1A", "surn2A", "surn3A", "surn4A", "Иванов", "surn6A", "surn7A", "surn8A", "surn9A", "surn10A"]
group2 = ["surn1B", "surn2B", "surn3B", "surn4B", "Иванов", "surn6B", "surn7B", "surn8B", "surn9B", "surn10B"]
for i in range(1, 3):
    random.shuffle(eval(f"group{i}"))
mix1, mix2 = zip(*random.sample(list(zip(group1, group2)), 5)) #* помогает передать кортежи в зип и это позволяет записывать результат в микс1 и микс2
sport = tuple(mix1 + mix2)
print("first group:", group1, "\nsecond group:", group2, "\nsport team: ", sorted(sport), "length:", len(sport), "\nivanov in sport team:", sport.count("Иванов"))