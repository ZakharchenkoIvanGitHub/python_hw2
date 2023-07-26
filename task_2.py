"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def decimal_to_hexadecimal(num: int) -> str:
    """
    Медод перевода десятичного представления числа в шестнадцатеричное
    :param num: десятичное представление
    :return: шестнадцатеричное представление
    """
    # Проверка на ноль
    if num == 0:
        return "0"

    # Список для хранения символов
    hex_chars = "0123456789abcdef"

    # Хранение шестнадцатеричного представления
    hexadecimal = ""

    # Перевод в шестнадцатеричную систему счисления
    while num > 0:
        remainder = num % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        num = num // 16

    return "0x"+hexadecimal


# Ввод числа
number = int(input("Введите целое число: "))

# Вызов функции для получения шестнадцатеричного представления
hexadecimal_representation = decimal_to_hexadecimal(number)

# Вывод результата
print(f"Шестнадцатеричное представление моим методом: {hexadecimal_representation}")
print(f"Шестнадцатеричное представление методом hex: {hex(number)}")
