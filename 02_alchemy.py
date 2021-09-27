# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Water:
    def __init__(self):
        self.name = "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Steam(part1=self, part2=other)
        else:
            return None


class Air:
    def __init__(self):
        self.name = "Воздух"

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lightning(part1=self, part2=other)
        else:
            return None


class Fire:
    def __init__(self):
        self.name = "Огонь"

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Air):
            return Lightning(part1=self, part2=other)
        else:
            return None


class Earth:
    def __init__(self):
        self.name = "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Air):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lava(part1=self, part2=other)
        else:
            return None


class Storm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм'


class Steam:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар'


class Dirt:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь'


class Lightning:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Молния'


class Dust:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль'


class Lava:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
print(water.name, '+', air.name, '=', Water() + Air())
print(water.name, '+', fire.name, '=', Water() + Fire())
print(air.name, '+', fire.name, '=', Air() + Fire())
print(air.name, '+', earth.name, '=', Air() + Earth())
print(water.name, '+', earth.name, '=', Water() + Earth())
print(fire.name, '+', earth.name, '=', Fire() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
