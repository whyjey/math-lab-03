def last_digit_sum_and_product(a, b):
    # Отримуємо останні цифри чисел
    last_digit_a = a % 10
    last_digit_b = b % 10
    
    # Обчислюємо суму та добуток останніх цифр
    digit_sum = last_digit_a + last_digit_b
    digit_product = last_digit_a * last_digit_b
    
    return digit_sum, digit_product

# Зчитування вхідних даних від користувача
a = int(input("Введіть перше тризначне число: "))
b = int(input("Введіть друге тризначне число: "))

# Перевірка, чи є числа тризначними
if 100 <= a <= 999 and 100 <= b <= 999:
    digit_sum, digit_product = last_digit_sum_and_product(a, b)
    print(f"Сума останніх цифр: {digit_sum}")
    print(f"Добуток останніх цифр: {digit_product}")
else:
    print("Введіть, будь ласка, тризначні числа.")
import sys

def polygon_angle(n):
    if n < 3:
        return "Кількість кутів повинна бути більше 2."
    return (n - 2) * 180 / n

# Зчитування вхідних даних з командного рядка
if len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
        angle = polygon_angle(n)
        print(f"Величина внутрішнього кута правильного {n}-кутника: {angle} градусів.")
    except ValueError:
        print("Будь ласка, введіть ціле число для кількості кутів.")
else:
    print("Введіть кількість кутів як аргумент командного рядка.")
