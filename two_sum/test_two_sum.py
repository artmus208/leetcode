
from two_sum.two_sum import Solution
sol_tow_sum = Solution()

def test_two_sum():
    # Базовые кейсы
    assert sol_tow_sum.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert sol_tow_sum.two_sum([3, 2, 4], 6) == [1, 2]
    assert sol_tow_sum.two_sum([3, 3], 6) == [0, 1]

    # Отрицательные числа и положительные
    assert sol_tow_sum.two_sum([-1000, -999, -123, 0, 1, 2, 456, 522, 100], 399) == [2, 7]
    assert sol_tow_sum.two_sum([-9, 12, -5, 14, -100, 874], 774) == [4, 5]

    # Пограничные значения
    assert sol_tow_sum.two_sum([0, 4, 3, 0], 0) == [0, 3]
    assert sol_tow_sum.two_sum([1, 10^9 - 1], 10^9) == [0, 1]

    # Большие числа
    assert sol_tow_sum.two_sum([10**6, 999_999, 1], 1_000_000) == [1, 2]

    # Очень длинный список с решением в конце
    long_list = list(range(10000)) + [12345, 54321]
    assert sol_tow_sum.two_sum(long_list, 66666) == [10000, 10001]

    # Нули
    assert sol_tow_sum.two_sum([0, 0, 3, 4], 0) == [0, 1]

    # Порядок индексов не важен, но результат должен быть корректен
    result = sol_tow_sum.two_sum([1, 5, 7, 3], 8)
    assert sorted(result) == [0, 2]
    