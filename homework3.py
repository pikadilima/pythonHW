# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# x = [2, 3, 5, 9, 3]
# sum1 = 0
# for i in range(1, len(x), 2):
#         sum1 += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях равна: {sum1}")


# my_list = [2, 3, 5, 9, 3, 5, 8, 9]
# print(sum(my_list[1::2]))

# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# my_list = [2, 3, 4, 5, 6]
# result_list = []
# for i in range((len(my_list)+1)//2):
#     result_list.append(my_list[i]*my_list[len(my_list)-1-i])
# print(result_list)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
#  минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# print(bin(n)[2:])

# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# # while n != 0:
# #     s = str(n%2) + s
# #     n //=2
# # print(s)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# ## Вариант 1
# def nega_fibonacci(n):
#     list_negafibonacci = [0]
#     if n == 0: 
#         return list_negafibonacci
#     elif n == 1:
#         list_negafibonacci = [1, 0, 1]
#         return list_negafibonacci    
#     else:
#         list_negafibonacci = [-1, 1, 0, 1, 1]
#         fib1 = fib2 = 1
#         for i in range(2, n):
#             fib1, fib2 = fib2, fib1 + fib2  # fib1 приравнивается к fib2, fib2 приравнивается к fib1 + fib2
#             list_negafibonacci.append(fib2)
#             list_negafibonacci.insert(0, (fib2 * (-1) ** i))
#         return list_negafibonacci
# n = int(input("Введите число: "))
# print((f"Список чисел (нега)Фибоначчи для k = {n}: {nega_fibonacci(n)}"))


## Вариант 2

# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# def nega_fibonacci(n):
#     list_negafibonacci = [0]
#     for i in range(1, n + 1):
#         list_negafibonacci.append(fibonacci(i))
#         list_negafibonacci.insert(0, (fibonacci(i) * (-1) ** (i + 1)))
#     return list_negafibonacci


# n = int(input("Введите число: "))
# print(f"Список чисел (нега)Фибоначчи для k = {n}: {nega_fibonacci(n)}")
