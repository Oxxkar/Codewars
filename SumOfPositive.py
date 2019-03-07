# marzo 07, 2019


def positive_sum(arr):
    max_sum = 0
    for num in arr:
        if num > 0:
            max_sum += num
    return max_sum
