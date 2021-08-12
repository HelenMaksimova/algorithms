"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""


def reverse_number(number, reversed_num=''):
    if not number:
        return reversed_num
    num = number % 10
    number = number // 10
    reversed_num = reversed_num + str(num)
    return reverse_number(number, reversed_num)


user_num = int(input('Введите число, которое требуется перевернуть: '))
print(f'Перевёрнутое число: {reverse_number(user_num)}')
