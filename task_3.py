"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction
import math


def add_fractions(fraction1: str, fraction2: str) -> tuple[str, str]:
    """
    Метод возвращающий сумму и произведение дробей
    :param fraction1: первая дробь
    :param fraction2: вторая дробь
    :return: сумма и произведение дробей
    """
    # Разделение и приведение числителя и знаменателя к целочисленному типу
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    # Вычисление суммы дробей
    sum_num = (num1 * denom2) + (num2 * denom1)
    sum_denom = denom1 * denom2

    # Вычисление произведения дробей
    product_num = num1 * num2
    product_denom = denom1 * denom2

    # Возвращение суммы и произведения в виде дробей
    return f"{int(sum_num / math.gcd(sum_num, sum_denom))}/" \
           f"{int(sum_denom / math.gcd(sum_num, sum_denom))}", \
           f"{int(product_num / math.gcd(product_num, product_denom))}/" \
           f"{int(product_denom / math.gcd(product_num, product_denom))}"


# Пример использования программы
fraction_1 = input("Введите первую дробь: ")
fraction_2 = input("Введите вторую дробь: ")

sum_fraction, product_fraction = add_fractions(fraction_1, fraction_2)
print(f"Сумма дробей моим методом: {sum_fraction}")
print(f"Произведение дробей моим методом: {product_fraction}")

print(f"Сумма дробей с использованием модуля fractions: {Fraction(fraction_1) + Fraction(fraction_2)}")
print(f"Произведение дробей с использованием модуля fractions: {Fraction(fraction_1) * Fraction(fraction_2)}")
