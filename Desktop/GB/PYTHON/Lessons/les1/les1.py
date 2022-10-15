# задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44

# a = input('Введите число ')

# def summa(a):                            
#     if float(a) < 0:                            
#         a = float(a) * (-1)
#     number = 0

#     for i in str(a):
#         if i != '.':             #работает с .
#             number += int(i)
#     return number

   
# print(f'Сумма чисел равна {summa(a)}')



# задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def set_products(n: int) -> list:
#     set = [1]
#     for i in range(2, n+1):
#         set.append(set[-1] * i)
#     return set

# n = int(input('Введите натуральное число: '))
# set = set_products(n)
# print(set)




# задача 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# # Пример:

# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06


# a = int(input('Введите число: '))
# lst = [round((1+1/n)**n, 2) for n in range(1, a+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 2)}')



# Задача 4. Задайте список из элементов, заполненных числами из промежутка [-N, N]. Задайте два числа - позиции(индексы) в исходном списке это границы диапазона. 
# Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:
# N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для [4, 1, 4, 1] равно 16


# from random import randint
# numbers = []
# for i in range(10):
#     numbers.append(randint (-10,10))
# print(numbers)

# def get_numbers(numbers):
#     count =0 
#     for element in numbers:
#         count +=1
#     return count
# print('Количество элементов: ', get_numbers(numbers))

# x = int(input('ВВедите первый элемент: '))
# y = int(input('Введите второй элемент: '))

# for i in range(len(numbers)):
#     mult = numbers[x -1]*numbers[y - 1]
# print(f'Сумма элементов: {numbers[x -1]} * {numbers[y -1]} =', mult)


# Задача 5. Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно.

import random
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Оснвоной список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)