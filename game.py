"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
from typing import Callable

import numpy as np


def find_predict(number: int = 1, low: int = 1, high: int = 100) -> int:
    """Функция поиска заданного числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        low (int, optional): Минимальное значение диапазона генерации числа. Defaults to 1.
        high (int, optional): Максимальное значение диапазона генерации числа. Defaults to 100.

    Returns:
        int: Количество попыток, которое потребовалось для угадывания числа
    """
    count = 0
    while True:
        count += 1
        # Алгоритм бинарного поиска числа
        if low + (high - low) // 2 < number:
            low = low + (high - low) // 2 + 1
        elif low + (high - low) // 2 > number:
            high = low + (high - low) // 2
        else:
            # Здесь мог производиться возврат найденного числа, если бы это было нужно
            break
    return count


def score_game(predict: Callable, low: int = 1, high: int = 100) -> int:
    """
    За какое количество попыток в среднем за 1000 подходов угадывает число алгоритм

    Args:
        predict (Callable): Алгоритм угадывания/поиска числа, с фиксацией количества попыток
        low (int, optional): Минимальное значение диапазона генерации числа. Defaults to 1.
        high (int, optional): Максимальное значение диапазона генерации числа. Defaults to 100.

    Returns:
        int: Количество попыток, которое потребовалось для угадывания числа
    """
    count_ls = []
    #np.random.seed(1)  # Задание конкретного seed при необходимости воспроизводимости результатов
    random_array = np.random.randint(low, high + 1, size=1000)  # Создание списка чисел для угадывания алгоритмом

    # Проверка и сохранение количества попыток для каждого числа
    for number in random_array:
        count_ls.append(predict(number, low, high))

    # Получение среднего значения количества попыток и вывод на экран
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")

    return score


if __name__ == "__main__":
    # RUN
    score_game(find_predict)
