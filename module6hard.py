# Задание "Они все так похожи"
import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled = False):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def  __is_valid_color(self, r, g, b):
        for i in r, g, b:
            if isinstance(i, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return r, g, b

    def set_color(self,r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        for j in new_sides:
            if isinstance(j, int) and len(new_sides) == self.sides_count:
                return True
            else:
                return False
    def get_sides(self):
        if self.sides_count == 12:
            return [self.__sides[0]] * self.sides_count
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius, *sides):
        super().__init__(color, *sides)
        self.__radius = radius

    def get_square(self):
        S_circle = self.__radius ** 2 * 3.14
        return S_circle

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        storoni = []
        super().__init__(color, *sides)
        for k in sides:
            storoni.append(k)
        sum1 = sum(storoni)
        max1 = max(storoni)
        self.max1 = max1
        p = 0.5 * sum1
        __height = 2 * math.sqrt(p * (p - storoni[0]) * (p - storoni[1]) * (p - storoni[2])) / self.max1
        self.__height = __height

    def get_square(self):
        S_triangle = 0.5 * self.max1 * self.__height
        return S_triangle

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__side = sides

    def get_volume(self):
        S_cube = self.__side ** 3
        return S_cube


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())