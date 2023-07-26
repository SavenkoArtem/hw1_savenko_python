# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter number: '))
flag = False
x = 2

for i in range(1, n):
    if flag != True:
        x = x ** i
        if x <= n:
            print(x, end=" ")
            x = 2
        else:
            print()
            flag = True