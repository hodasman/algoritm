"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num = enter_num // 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4 (enter_num):
    lst = []
    for i in range(len(str(enter_num))):
        lst.append(str(enter_num % 10))
        enter_num //= 10
    return ''.join(lst)

num = 3587
print(timeit('revers(num)', globals=globals()))
print(timeit('revers_2(num)', globals=globals()))
print(timeit('revers_3(num)', globals=globals()))
print(timeit('revers_4(num)', globals=globals()))

print(revers(3581), revers_2(3581), revers_3(3581), revers_4(3581))