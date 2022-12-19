#
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#

# from math import pi
#
# d = input('Введите число: ').count('0')
# print(round(pi,d))


#
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
#
#
# n = int(input("Введите число N: "))
# my_list = []
# a = 2
# m = n
# while a * a <= n:
#         if n % a == 0:
#             my_list.append(a)
#             n//=a
#         else:
#             a += 1
# my_list.append(n)
# print(f'Список простых множителей: {my_list}')



# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#

# my_list = [1, 5, 5, 7, 9, 8, 9, 1, 1, 3]
# new_list = []
# for i in range(len(my_list)):
#     for j in range(len(my_list)):
#         if i != j and my_list[i] == my_list[j]:
#             break
#     else:
#         new_list.append(my_list[i])
# print(new_list)


#
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#

from random import randint

k = int(input("Введите степень k: "))

my_list = []
for i in range(1, k + 2):
    my_list.append(randint(1, 101))

new_list = []  # заполлняем список исходя из значения степени
for i in range(len(my_list)):
    if k == 1:
        new_list.append(f'{my_list[i]}*x+')
    elif k == 0:
        new_list.append(f'{my_list[i]}')
    else:
        new_list.append(f'{my_list[i]}*x^{k}+')
    k -= 1

my_list.append('=0')

with open('doc.txt', 'w') as data:
    data.write(''.join(new_list))
data.close()

#
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.