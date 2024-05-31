# 8.1)	Скачайте любую открытку из интернета, определите область,
# которую Вам нужно вырезать из данного изображения (обрезать текст, часть фото и т.д.).
# Напишите программу, которая выполнит эту операцию. Сохраните изображения в текущую папку под новым именем.
def fisrt():
    from PIL import Image
    img = Image.open("first.jpg")
    cut = img.crop((1, 1, 1500, 940))
    cut.save('resized_postcard.jpg')

# 8.2)	Создайте словарь, содержащий перечень пары «Название праздника – имя_файла с открыткой к нему».
# Спросите у пользователя, к какому празднику ему нужна открытка и выведите нужную открытку на экран.
def first1():
    from PIL import Image
    holidays = {
        "День рождения": "birthday_card.jpg",
        "Хэллоуин": "halloween.jpg",
        "Новый год": "new_year_card.jpg",
        "23 февраля": "23_february.jpg",
        "8 марта": "women_day_card.jpg",
        "Первое мая": "1_may.jpg",
        "Пасха": "easter_day.jpg"
    }
    ch = input("введите праздник: ")
    ch = ch.capitalize()
    if ch in holidays:
        card_name = holidays[ch]
        card_image = Image.open(card_name)
        card_image.show()
    else:
        print("открытки для данного праздника нет в базе")

def fisrt2():
    from PIL import Image, ImageDraw, ImageFont
    def create_holidays(text):
        img = Image.open("1.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("corbel.ttf", 50)
        width, height = draw.textsize(chfinal, font=font)
        width2 = 1332 - width
        height2 = 850 - height
        draw.text((width2/2, height2/2), text, fill=(110, 46, 35), font=font)
        img.show()
    holidays = {
        "День рождения": "1.jpg",
        "Хэллоуин": "1.jpg",
        "Новый год": "1.jpg",
        "23 февраля": "1.jpg",
        "8 марта": "1.jpg",
        "Первое мая": "1.jpg",
        "Пасха": "1.jpg"
    }
    ch = input("введите праздник: ")
    ch = ch.capitalize()
    if ch in holidays:
        card_name = holidays[ch]
        chfinal = "Ура! " + ch + ", поздравляем!"
        create_holidays(chfinal)
    else:
        print("пожеланий для вашего праздника нет в базе")
# 8.3)	Модифицируйте задачу 8.1 так: спросите еще у пользователя, имя того, кого он хочет поздравить,
# добавьте на заданную открытку текст  «….,  поздравляю!»,  где  вместо  ….  вставьте
# полученное имя (выведите его разным цветом и шрифтами, посередине вверху или внизу фото).
# Найдите в сети интернет решение, как сделать надпись жирным текстом (по умолчанию, такого параметра нет).
# Сохраните новую открытку в файл с расширением png.
def third():
    from PIL import Image, ImageDraw, ImageFont
    img = Image.open("first.jpg")
    cut = img.crop((1, 1, 1500, 940))
    name = input("как зовут получателя открытки? ")
    draw = ImageDraw.Draw(cut)
    font_name = ImageFont.truetype("D:\\Times_New_Roman_bold.ttf", 55)
    font_normal = ImageFont.truetype("D:\\timesnewromanpsmt.ttf", 45)
    fill_color_name = (140, 202, 152)
    fill_color_normal = (153, 230, 224)
    stroke_color = (20, 21, 20)
    width_name, height = draw.textsize(name, font=font_name)
    draw.text((1000 - width_name, 75), name, font=font_name, fill=fill_color_name, stroke_width=3, stroke_fill=stroke_color)
    draw.text((1000 + 5, 85), ",  поздравляю!", font=font_normal, fill=fill_color_normal, stroke_width=3, stroke_fill=stroke_color)
    cut.show()
    cut.save('third.png')

first1(), fisrt(), fisrt2(), third()