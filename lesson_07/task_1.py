"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import timeit


def bubble(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff


def bubble_refactor(array):
    n = len(array)
    for i in range(n-1):
        flag = True
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
                flag = False
        if flag:
            break


arr = [randint(-100, 99) for _ in range(20)]
print('Исходный массив:', arr)
bubble_refactor(arr)
print('Отсортированный массив:', arr)


# Замеры на массивах разной длины:

test_nums = (10, 100, 1000)

test_arrays = tuple([randint(-100, 99) for _ in range(num)] for num in test_nums)

print('\nОбычная функция:')
for arr in test_arrays:
    print(f'Массив на {len(arr)} элементов: {timeit("bubble(arr[:])", globals=globals(), number=1000)}')

print('\nДоработанная функция:')
for arr in test_arrays:
    print(f'Массив на {len(arr)} элементов: {timeit("bubble_refactor(arr[:])", globals=globals(), number=1000)}')

# Обычная функция:
# Массив на 10 элементов: 0.005127800000000002
# Массив на 100 элементов: 0.4298532
# Массив на 1000 элементов: 49.843064500000004
#
# Доработанная функция:
# Массив на 10 элементов: 0.0051964000000026545
# Массив на 100 элементов: 0.4547865999999985
# Массив на 1000 элементов: 52.677553

# Был реализован механизм прерывания обхода списка элементов, если за проход не было ни одной замены
# (то есть массив уже отсортирован).
# Замеры показывают, что при сортировке сформированных случайным образом массивов данная доработка не даёт
# никакой эффективности - напротив, она даже слегка замедляет работу алгоритма за счёт проверки дополнительных условий.
# Это происходит потому, что вероятность того, что в массиве эелементов, сформированном случайным образом, изначально
# окажется хоть сколько-нибудь длинная отсортированная последовательность, невелика. С увеличением количества элементов
# массива эта вероятность становится ничтожно малой.
# Если же рассматривать частично упорядоченные массивы, то данный механизм может привести к ускорению работы:

part_ordered_array = [randint(50, 100) for _ in range(50)] + [elem for elem in range(49, -1, -1)]

print(f'\nМассив на 100 элементов (обычная): {timeit("bubble(part_ordered_array[:])", globals=globals(), number=1000)}')
print(f'Массив на 100 элементов (доработанная): '
      f'{timeit("bubble_refactor(part_ordered_array[:])", globals=globals(), number=1000)}')

# Массив на 100 элементов (обычная): 0.28453779999999995
# Массив на 100 элементов (доработанная): 0.19400640000000002

# Как видно по замерам, если массив частично упорядочен, доработанная функция выполняет сортировку значительно быстрее.
