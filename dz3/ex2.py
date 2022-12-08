# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list =[]
for i in range (5):
    list.append(int(input("Введите элементы списка  ")))

new_list = []
for i in range(len(list) // 2 + len(list) % 2):
    new_list.append(list[i] * list[len(list) - 1 - i])
print(new_list)