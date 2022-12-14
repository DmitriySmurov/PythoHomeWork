# Задача 1. Вычислить число pi c заданной точностью d. Число d находится в интервале [1e-1, 1e-10]
# Пример:
# - при d = 0.001, pi = 3.141.
# Примечание:
# Использовать только итерационные алгоритмы вычисления числа pi. Любой на ваш выбор.

# Написать функцию, которая принимает аргумент: точность вычисления числа pi

# Возвращает:

# Вычисленное число pi
# Количество выполненных итераций
# Погрешность вычисления

# Пример вызова функции: - vallis(1e-4) -> (3.141392685883853, 3928, -0.00019996770594010727)



# import math

# pi = math.pi
# print( "Пи = ", pi)

# a = 0.001
# print(f"Точность = {a}")
# count = 0
# while a < 1:
#     count += 1
#     a = a*10
# print(round(pi, count))





# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.

# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];


# from turtle import clear


# a = int(input("Введите число: "))

# list =[]
# for i in range(1, a+1):
#     if(a%i==0):
#         list.append(i)
# print(f"{a} = {list}")



# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# import random

# list = [random.randint(0,15) for i in range (10)]
# print(list)

# new_list = []
# [new_list.append(i) for i in list if i not in new_list]
# print(new_list)



# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100

# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.

# Примечание Создать три функции:

# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином. Коэффициенты вычисляются случайными.
# Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
# В словаре степени будут ключами, в списке - индексами.
# Например k=3 => 6*x^3 + 4*x + 5. Словарь будет такой: {3:6, 2:0, 1:4, 0:5}. А список такой [5,4,0,6]

# 2) Функция формирование строки-полинома. Аргумент: полином (в вид словаря или списка).
# Возвращает строку вида '6*x^3 + 4*x + 5'
# Примечание: Обратите внимание на запись первой и нулевой степени, а также учет нулевого коэффициента.
# Для формирования строки удобно использовать join

# 3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином.

# import random


# def write_file(st):
#     with open('file1.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0,101)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))










