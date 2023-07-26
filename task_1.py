"""
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
"""
import math


def solve_quadratic_equation(a: float, b: float, c: float) -> tuple[float, float] | float | tuple[complex, complex]:
    """
    метод решения квадратного уравнения с отрицательным дискриминантом
    :param a: коэффициент a
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни уравнения
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        complex_solution1 = complex(real_part, imaginary_part)
        complex_solution2 = complex(real_part, -imaginary_part)
        return complex_solution1, complex_solution2


# Пример использования
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

solutions = solve_quadratic_equation(a, b, c)

# Вывод решений
print("Решения уравнения:")
for solution in solutions:
    print(solution)
