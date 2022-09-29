# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print(sum) 

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# from math import factorial


# n = int(input('Введите число N:'))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')


# 3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

# n = int(input('Введите число:'))
# list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# print(f'Последовательность: {list}\n Сумма: {round(sum(list))}')



# 4.Реализуйте алгоритм перемешивания списка.
# from random import shuffle
# import random
# my_list = [1 , 2, 3, 4, 5]
# print(my_list)
# random.shuffle(my_list)
# print(my_list)

# my_list = [1 , 2, 3, 4, 5]
# print(my_list)
# my_list.reverse()
# print(my_list)

