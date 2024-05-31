# 4.1)	Напишите функцию, которая проверяет, делится ли введенное число на 3, или нет.
def fisrt():
    a = int(input("vvedite chislo "))
    def is_the_number_divisible(a):
        return True if ((a % 3 == 0) or (a == 0)) else False
    print(is_the_number_divisible(a))

# 4.2)	Напишите программу деления числа 100 на введенное пользователем число.
# Деление реализуйте с помощью функции. Предусмотрите возможные исключения
# (ValueError, возникающее в случае, если пользователь введет не число, а строку, и ZeroDivisionError – если будет введено число 0 и остальные).
def seccond():
    try:
        a = 100
        b = int(input("vvedite chislo "))
        print(a//b)
    except ZeroDivisionError:
        print('error! deleniye na 0')
    except ValueError:
        print('error! vvedeno strokovoye znacheniye')

# 4.3)	Напишите функцию, которая возвращает True, если введенная пользователем дата является магической,
# False в обратном случае. Магической считается дата, в которой произведение дня и месяца равно двум последним цифрам года, например: 02.11.2022.
def ththth():
    def is_the_year_magick(day, year, month):
        return day * month == year
    day = int(input("input day "))
    year = (int(input("input year ")) % 100)
    month = int(input("input month "))
    print(is_the_year_magick(day, year, month))

# 4.4)"Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме второй половины цифр.
# Номера могут быть произвольной длины, с единственным условием, что количество цифр всегда чётно, например: 33 или 2341 и так далее.
# Билет с номером 385916 — счастливый, так как 3+8+5 == 9+1+6. Билет с номером 231002 не является счастливым, так как 2+3+1!= 0+0+2
# Реализуйте функцию, проверяющую является ли номер счастливым (номер — всегда строка).
import random
# import sys
ticket = str(random.randint(10, 9999))
# ticket = str(random.randint(10, sys.maxsize))
if len(ticket) % 2 != 0:
    print("bilyet chetny")
else:
    mid = len(ticket) // 2
    sum1 = sum(int(i) for i in ticket[:mid])
    sum2 = sum(int(i) for i in ticket[mid:])
    print("bilet shastlivy! ego nomer:", ticket) if sum1 == sum2 else print("bilet ne scactlivy! ego nomer:", ticket)
