# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input("Введите день недели от 1 до 7:"))
# if 0<a<6:
#     print ("рабочий день")
# else:
#     print ("выходной день")

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений 
# предикат.
# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))

# a = x * y * z
# b = x + y + z

# if a > 0:
#     a = 0
# elif a < 1:
#     a = 1
# if b > 0:
#     b = 1
# elif b < 1:
#     b = 1

# if a == b:
#     print('Утверждение истинно')
# elif a != b:
#     print('Утверждение ложно')

# leftSide = not (x or y or z)
# rightSide = not x and not y and not z
# result = leftSide == rightSide

# if result == True:
#     print('Утверждение истинно')
# else:
#     print('Утверждение ложно')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input("Введите координату X:"))
# y = int(input("Введите координату Y:"))
# if x>0 and y>0:
#     print ("Координаты соответствуют первой четверти")
# elif x<0 and y>0:
#     print ("Координаты соответствуют второй четверти")
# elif x<0 and y<0:
#     print ("Координаты соответствуют третьей четверти")
# elif x>0 and y<0:
#     print ("Координаты соответствуют четвертой четверти")

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).
# a = int(input("Введите четверть от 1 до 4:"))
# if a == 1:
#     print ("Координаты x>0, y>0")
# elif a == 2:
#     print ("Координаты x<0, y>0")
# elif a == 3:
#     print ("Координаты x<0, y<0")
# elif a == 4:
#     print ("Координаты x>0, y<0")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# import math
# x1 = int(input("Введите координату X 1  точки:"))
# y1 = int(input("Введите координату Y 1 точки:"))
# x2 = int(input("Введите координату X 2 точки:"))
# y2 = int(input("Введите координату Y 2 точки:"))
# dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
# print (dist)