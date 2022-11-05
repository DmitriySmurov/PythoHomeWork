# задача 1. Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста


# with open('incoming_text_01.txt', 'w', encoding='UTF-8') as file:
#     file.write(input("Введите текст: "))
# with open('incoming_text_01.txt', 'r',) as file:
#     my_text = file.readline()
#     change_text = my_text.split()
# print()
# print(my_text)
# print()

# del_text = input("Введите набор букв, которые нужно уддалить из текста:  ")
# print(del_text)

# result = ' '.join(filter(lambda x: del_text not in x, change_text))
# with open('format_text_01.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{result}')
#     print(result)




# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит некоторое кол-во конфет, например 220.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, которые точно определят победу.


# import random
# name1 = input("Ввведите имя певрого игрока: ")
# name2 = input("Ввведите имя второго игрока: ")
# igrok = random.randrange(1,3)
# a = int(input("Введите колличество конфет: "))
# if igrok ==1:
#     print("Первый ход делает ", name1)
# else:
#     print("Первый ход делает ", name2)

# while a > 0:
#     if a> 28:
#         igrok1 = int(input("Ты можешь взять не больше 28 конфет, сколько конфет ты взял? "))
#         a = a - igrok1
#         if a > 28:
#             igrok2 = int(input("Ты можешь взять не больше 28 конфет, сколько конфет ты взял? "))
#             a = a - igrok2
#             if a <= 28:
#                 if igrok ==1:
#                     print("Осталось ", a, "шт их забирает", name1, "a значит ПОБЕДИЛ", name1)
#                 else:
#                     print("Осталось ", a, "шт их забирает", name2, "a значит ПОБЕДИЛ", name2)
#         else:
#             if igrok ==1:
#                 print("Осталось ", a, "шт их забирает", name2, "a значит ПОБЕДИЛ", name2)
#             else:
#                 print("Осталось ", a, "шт их забирает", name1, "a значит ПОБЕДИЛ", name1)




# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# https://ru.wikipedia.org/wiki/Кодированиедлинсерий

# Создать функцию сжатия строки и функцию восстановления строки.

# Пример:
# ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR

# with open('text_for_RLE_51.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('text_for_RLE_51.txt', 'r') as file:
#     my_text = file.readline()
#     text_compression = my_text.split()

# print(my_text)


# def rle_encode(text):
#     enconding = ''
#     prev_char = ''
#     count = 1
#     if not text:
#         return ''

#     for char in text:
#         if char != prev_char:
#             if prev_char:
#                 enconding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         enconding += str(count) + prev_char
#         return enconding


# text_compression = rle_encode(my_text)

# with open('text_compression_RLE_51.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{text_compression}')
# print(text_compression)