# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число
# .

import random

n = int(input('Введите количество элементов: '))
list = []
for i in range(n):
    list.append(random.randint(-n, n))


p = 1
new_list = []

with open('file.txt', 'r') as file:
    for line in file:
        if -len(list) <= int(line) < len(list):
            p *= list[int(line)]
            new_list.append(list[int(line)])

print('Созданный список: ', list)
print('Новый список: ', new_list)
print('Произведение элементов = ', p)

