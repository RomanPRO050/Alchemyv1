# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
global pug


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 30
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='grey')
        self.house.money += 150
        self.fullness -= 10

    def play_f1_2021(self):
        cprint('{} играл в F1 2021 целый день на XBOX'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.house.dirt >= 100:
            self.clean_the_house()
        if self.fullness < 20:
            self.eat()
        if self.house.pug_food <= 20:
            self.buy_food_for_pug()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_f1_2021()

    def move_into_the_house(self, house):
        self.house = house
        cprint('{} заехал в дом!!!!'.format(self.name), color='cyan')
        self.fullness -= 10

    def pick_up_the_pug(self, house, name):
        global pug
        pug = Pug(house, name)
        cprint('{} взял мопса в дом!!!!'.format(self.name), color='red')
        self.fullness -= 10

    def buy_food_for_pug(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за камушками Леониду Васильевичу'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.pug_food += 50

    def clean_the_house(self):
        cprint('{} убрался в доме..'.format(self.name), color='magenta')
        self.house.dirt -= 100
        self.fullness -= 10


class House:
    def __init__(self):
        self.food = 20
        self.money = 50
        self.pug_food = 0
        self.dirt = 1

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, камушков для мопса {}, загрязненность в доме {}'.format(
            self.food, self.money, self.pug_food, self.dirt)


class Pug:
    def __init__(self, house, name):
        self.name = name
        self.fullness = 40
        self.house = house

    def __str__(self):
        return 'Я - мопс {}, сытость {}'.format(
            self.name, self.fullness)

    def sleep(self):
        self.fullness -= 5

    def walk(self):
        self.fullness -= 10
        self.house.dirt += 10

    def eat(self):
        if self.house.pug_food >= 20:
            self.fullness += 20
            self.house.pug_food -= 20
        else:
            cprint('Нет еды у мопса', color='red')

    def poop(self):
        self.fullness -= 5
        self.house.dirt += 10

    def act(self):
        if self.fullness <= 0:
            cprint('{} мопс умер...'.format(self.name), color='red')
            return

        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
            k = 0
            k += 1
            if k % 2 == 0:
                self.poop()
        elif dice == 1:
            cprint('{} покушал'.format(self.name))
            self.eat()
        elif dice == 2:
            cprint('{} вздремнул'.format(self.name))
            self.sleep()
        elif dice == 3:
            cprint('{} погулял'.format(self.name))
            self.walk()
        elif dice == 4:
            cprint('{} покушал'.format(self.name))
            self.sleep()
        elif dice == 5:
            cprint('{} погулял'.format(self.name))
            self.walk()
        elif dice == 6:
            cprint('{} сделал пупи'.format(self.name))
            self.poop()


vasya = Man(name='Вася')
my_sweet_home = House()
vasya.move_into_the_house(house=my_sweet_home)
vasya.pick_up_the_pug(house=my_sweet_home, name=input())
vasya.buy_food_for_pug()

for day in range(1, 365):
    cprint('=================== день {} ==================='.format(day), color='yellow')
    vasya.act()
    pug.act()
    cprint('------------------в конце дня--------------------'.format(day))
    print(vasya)
    print(pug)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
