from abc import ABC, abstractmethod
import math
class Figure(ABC):
    def __init__(self, nameFigure, colorFigure):
        self.nameFigure = nameFigure
        self.color = colorFigure

    @abstractmethod
    def findSquare(self):
        pass

class Circle(Figure):
    def __init__(self,nameFigure, colorFigure, radius):
        super().__init__(nameFigure, colorFigure)
        self.radius = radius

    def findSquare(self):
        print(f'Площадь {self.nameFigure}: {math.pi * math.pow(self.radius, 2)}')


class Triangle(Figure):
    def __init__(self,nameFigure, colorFigure, a, h):
        self.a = a
        self.h = h
        super().__init__(nameFigure, colorFigure)

    def findSquare(self):
        sq = 0.5 *(self.a * self.h)
        print(f'Площадь {self.nameFigure}: {sq}')


class square(Figure):
    def __init__(self,nameFigure, colorFigure, m, n):
        self.m = m
        self.n = n
        super().__init__(nameFigure, colorFigure)

    def findSquare(self):
        kv = self.m*self.n
        print(f'Площадь {self.nameFigure}: {kv}')

class rhombus(Figure):
    def __init__(self,nameFigure, colorFigure, k,l,j,i):
        self.k = k
        self. l= l
        self.i = i
        self.j = j
        super().__init__(nameFigure, colorFigure)

    def findSquare(self):
        bn = (self.l*self.k*self.i*self.l)/2
        print(f'Площадь {self.nameFigure}: {bn}')


c1 = Circle('Большой круг', 'красный', 4)
c1.findSquare()

t1 = Triangle('Треугольник в Египте', 'Желтый', 4, 6)
t1.findSquare()
s1=square('Треуго', 'Желтый', 4, 6)
s1.findSquare()


"""
Создать классы Square, Romb, RightTriangle

#Найти площать квадрата

#Найти площадь ромба

#Найти площадь равнобедренного треугольника
"""






