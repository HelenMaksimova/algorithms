"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

from random import randint


def min_element_1(number_list: list) -> int:
    """
    Функция возвращает значение минимального элемента из списка целых чисел
    :param number_list: список целых чисел
    :return: целое число
    Сложность: квадратичная
    """
    min_number = number_list[0]
    for number in number_list:
        for item in number_list:
            if number < item and number < min_number:
                min_number = number
    return min_number


def min_element_2(number_list: list) -> int:
    """
    Функция возвращает значение минимального элемента из списка целых чисел
    :param number_list: список целых чисел
    :return: целое число
    Сложность: линейная
    """
    min_number = number_list[0]
    for number in number_list:
        if number < min_number:
            min_number = number
    return min_number


test_list = [randint(-10, 100) for _ in range(20)]

print(test_list)

print('Результат работы первой функции: ', min_element_1(test_list))
print('Результат работы второй функции: ', min_element_2(test_list))
print('Результат работы встроенной функции min: ', min(test_list))
