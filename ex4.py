# 4.	Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти '))
if number == 1:
    print('Диапазон координат точек в первой четверти x > 0 и y > 0')
elif number == 2:
    print('Диапазон координат точек во второй четверти x < 0 и y > 0')
elif number == 3:
    print('Диапазон координат точек в третьей четверти x < 0 и y < 0')
elif number == 4:
    print('Диапазон координат точек в четвертой четверти x > 0 и y < 0')
else:
    print('Диапазон не найден')
