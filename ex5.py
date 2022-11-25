from math import sqrt
# 5.	Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# o	A (3,6); B (2,1) -> 5,09
# o	A (7,-5); B (1,-1) -> 7,21



a1 = int(input('Введите а1'))
a2 = int(input('Введите а2'))
b1 = int(input('Введите b1'))
b2 = int(input('Введите b2'))

xc = float(a1 - b1) * float(a1-b1)
yc = float(a2-b2) * float(a2-b2)
res = float(sqrt(xc + yc))
res = int(res * 100) / 100
print(res)

