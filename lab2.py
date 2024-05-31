# 12.1) При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход
# уменьшает возможность неверного ввода пароля. Напишите программу, которая сравнивает пароль и его подтверждение.
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
def fffff():
    import re
    import secrets
    import string
    ch = 0
    strong = r'(?=(.*[a-z]))(?=(.*[A-Z]))(?=(.*[0-9]))(?=(.*[!@#$%^&*()\-__+.])).{8,}'
    passworduser = input("vvedite paryol: ")
    match = re.search(strong, passworduser)
    if match:
        print("paryol normalnyi")
    else:
        print("paryol dolzhen soderzhat zaglavniye i strochniye bykvi, cifry, specialniye symvoly")
        ch = 1
    if ch == 0:
        passworduser2 = input("povtoritye paryol: ")
        if passworduser != passworduser2:
            print("paryol ne prinyat")
            exit()
#проверка слили ли пароль (можно убрать?), passpwnedcheck библиотека
    if ch == 0:
        from passpwnedcheck.pass_checker import PassChecker
        pass_checker = PassChecker()
        password = passworduser
        is_leaked, count = pass_checker.is_password_compromised(password)
        if is_leaked:
            print('vash paryol byl slit {count} raz')
            ch = 1
        else:
            print('vash paryol pryniat')
#генерация
    if ch == 1:
        check = input("vi hotite sgenerirovat novi paryol? ")
        if (check == "yes" or check == "da"):
            symb = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            print(''.join(secrets.choice(symb) for i in range(16)))
        else:
            exit()


#2.2) Напишите программу, которая определяет, какой тип места в плацкартном вагоне (верхнее или нижнее, в плацкарте или боковое) по заданному номеру места.
def twtwtw():
    import random
    s = random.randint(1, 54)
    pl = "verhnee" if s % 2 == 0 else "nizhnee"
    if 37 <= s:
        print("seat num:", s, pl, "res: bokovoye sidenye")
    else:
        print("seat num:", s, pl, "res: placart")


#2.3) Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
#Напишите функцию, которая определяет, является ли год с данным номером високосным.
# Если год является високосным, то выведите «Год ... - високосный», где вместо многоточия выведите год, иначе выведите «Это год не високосный».
def ththth():
    num = int(input("vvedite god: "))
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print("visokocny")
    else:
        print("ne visokosny")


# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
# - если смешать красный и синий, то получится фиолетовый;
# - если смешать красный и желтый, то получится оранжевый;
# - если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит
# что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.
def chchch():
    import random
    colors = ["red", "blue", "yellow"]
    num1 = random.randint(0, 2)
    num2 = random.randint(0, 2)
    if num1 == num2:
        print("used colors:", {colors[num1]}, {colors[num2]}, "res:", {colors[num1]})
    else:
        mixed_color = "violet" if {num1, num2} == {0, 1} else "orange" if {num1, num2} == {0, 2} else "green" if {num1, num2} == {1, 2} else 'no res'
        print("used colors:", {colors[num1]}, {colors[num2]}, "res:", {mixed_color})

fffff(), twtwtw(), ththth(), chchch()