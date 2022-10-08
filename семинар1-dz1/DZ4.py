# 4. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

print("Введите координаты точки A:")
x_A = float(input("X: "))
y_A = float(input("Y: "))
print("Введите координаты точки B:")
x_B = float(input("X: "))
y_B = float(input("Y: "))

from math import sqrt
print('Distance between A and B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2)) # Теорема Пифагора