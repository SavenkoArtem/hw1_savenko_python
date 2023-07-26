# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

x = int(input('Enter X от 1 до 1000 '))
y = int(input('Enter Y от 1 до 1000 '))


if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Enter x and y values from 1 to 1000')
else:
    S = x + y
    P = x * y
    flag = False

    for i in range(1, 1001):
        if flag != True:
            for j in range(1, 1001):
                if flag != True:
                    if i * j == P and i + j == S:
                        print(f"res = {i} and {j}")
                        flag = True 