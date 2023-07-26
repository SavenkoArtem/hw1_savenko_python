# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

quantity_coin = int(input('Enter the number of coins: '))
orel = 0
reshka = 0

for i in range(quantity_coin):
    enter_value = int(input('Enter 1 - orel or 0 - reshka: '))
    if enter_value == 1:
        orel += 1
    else:
        reshka += 1

if orel < reshka:
    print(f'Flip {orel} coins')    
else:
    print((f'Flip {reshka} coins'))