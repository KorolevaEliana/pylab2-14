# 9.1)	Модифицируйте программу из практики 7.3 (7 лабораторная работа )
# или создайте заново: обработать любой операцией все картинки в заданной папке, используя для обхода файлов в папке модуль os (или Pathlib).
# При этом каталог для итоговых (обработанных) изображений должен тоже создаваться с помощью модуля os или Pathlib.
def first():
    from PIL import Image, ImageFilter
    from pathlib import Path
    for i in range(1, 6):
        orig = Image.open(Path(f"{i}.jpg"))
        filt = orig.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 12, -1, -1, -1, -1), 1, 0))
        filt.save(Path(Path.home()) / "newphotos" / f"filter{i}.jpg")
# 9.2)	Модифицировать программу из практики 9.1, добавив проверку типа (расширения) файла, если в папке хранятся разные типы файлов,
# а вам нужно обработать только заданные (jpg, png)
def second():
    from PIL import Image, ImageFilter
    from pathlib import Path
    for i in range(1, 6):
        orig = Image.open(Path(f"{i}.jpg"))
        if (Path(f"{i}.jpg").suffix == '.jpg') or (Path(f"{i}.jpg").suffix == '.png'):
            filt = orig.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 12, -1, -1, -1, -1), 1, 0))
            filt.save(Path(Path.home()) / "newphotos" / f"filter{i}.jpg")
        else:
            print(f"{i} file: incorrect file type")
# 9.3)	Имеется файл с данными в формате csv:
# Продукт,Количество,Цена Молоко,2,80
# Сыр,1,500
# Хлеб,2,70
# Напишите программу, которая считывает данные из этого файла, подсчитывает итоговую сумму расходов и выводит данные в виде:
# Нужно купить:
# Молоко - 2 шт. за 80 руб. Сыр - 1 шт. за 500 руб.
# Хлеб - 2 шт. за 70 руб. Итоговая сумма: 800 руб.
def third():
    import csv
    items = []
    cost = 0
    with open("lab9.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            Продукт, Количество, Цена = row
            cost2 = int(Количество) * int(Цена)
            items.append(f"{Продукт} - {Количество} шт. за {Цена} руб.")
            cost += cost2
    print("Нужно купить:\n", " ".join(items), f"Итоговая сумма: {cost} руб.")

third()