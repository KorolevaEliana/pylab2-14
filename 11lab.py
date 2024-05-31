#11.1)	Задача «Ресторан»: создайте класс с именем Restaurant.
# Метод init () класса Restaurant должен содержать два атрибута: restaurant_name (название ресторана) и cuisine_type (тип кухни).
# Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем newRestaurant. Выведите два атрибута по отдельности, затем вызовите оба метода.
def first():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restuarant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def open_restaurant(self):
            return f"ресторан '{self.restuarant_name}' '{self.cuisine_type}' кухня открылся"
        def describe_restaurant(self):
            description = f"ресторан '{self.restuarant_name}' кухня '{self.cuisine_type}'"
            return description

    newRestaurant = restaurant("круто", "китайская")

    restaurant_description = newRestaurant.describe_restaurant()
    restaurant_open_message = newRestaurant.open_restaurant()
    print(restaurant_open_message)
    print(restaurant_description)

# 11.2)	На основе ранее созданного класса Restaurant из задания 11.1 создайте три разных экземпляра (три ресторана),
# вызовите для каждого экземпляра метод describe_restaurant().
def second():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restuarant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            description = f"ресторан '{self.restuarant_name}' кухня '{self.cuisine_type}'"
            return description
    restaurant1 = restaurant("рестик1", "национальная")
    restaurant2 = restaurant("рестик2", "европейская")
    restaurant3 = restaurant("рестик3", "армянская")
    description1 = restaurant1.describe_restaurant()
    description2 = restaurant2.describe_restaurant()
    description3 = restaurant3.describe_restaurant()
    print("первый ресторан: ", description1, "\nвторой ресторан: ", description2, "\nтретий ресторан: ", description3)




#11.3)	Добавьте в созданный класс Restaurant атрибут, задающий начальный рейтинг ресторана и метод,
# который получает на вход новое значение рейтинга и обновляет его.
import random
class restaurant:
    def __init__(self, restaurant_name, cuisine_type, restaurant_rating):
        restaurant_rating = 0
        self.restaurant_rating = restaurant_rating
        self.restuarant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def open_restaurant(self):
        return f"ресторан '{self.restuarant_name}' '{self.cuisine_type}' кухня с рейтингом '{self.restaurant_rating}' открылся"
    def describe_restaurant(self):
        description = f"ресторан '{self.restuarant_name}' кухня '{self.cuisine_type}' рейтинг '{self.restaurant_rating}"
        return description
    def rate_restaurant(self, updrate):
        self.restaurant_rating = updrate
        return f'рейтинг обновлен: {updrate}'

newRestaurant = restaurant("круто", "китайская", 56)
print(newRestaurant.describe_restaurant())
updrate = random.randint(1, 5)
message = newRestaurant.rate_restaurant(updrate)
print(message)
print(newRestaurant.describe_restaurant())
