# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# o	6 -> да
# o	7 -> да
# o	1 -> нет

day = int(input('Введите день недели: '))
if day == 6 or day == 7:
    print('Выходной')
elif day<6 and day>=1:
    print('Рабочий')
else:
    print('Это не день недели')