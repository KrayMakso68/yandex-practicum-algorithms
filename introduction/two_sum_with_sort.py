def two_sum_with_sort(values: list, target_sum: int) -> list:
    values.sort()
    left = 0
    right = len(values) - 1
    while left < right:
        current_sum = values[left] + values[right]
        if current_sum == target_sum:
            return [values[left], values[right]]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    input()
    values = list(map(int, input().split()))
    target_sum = int(input())
    result = two_sum_with_sort(values, target_sum)
    print(' '.join(map(str, result)) if result else None)