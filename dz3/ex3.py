# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_dif(list):
    for i in range(len(list)):
        list[i] = (list[i] % 1)
        result = round(max(list) - min(list),2)
    return f'Результат: {result}'




list =[]
for i in range (5):
    list.append(float(input("Введите элементы списка  ")))

print(find_dif(list))

