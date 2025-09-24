def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

assert sum_list([1, 2, 3, 4, 5]) == 15
assert sum_list([-1, 0, 1]) == 0