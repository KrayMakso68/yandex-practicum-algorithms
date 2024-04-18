def two_sum_naive(values: list, target_sum: int) -> list:
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target_sum:
                return [values[i], values[j]]
if __name__ == '__main__':
    input()
    values = list(map(int, input().split()))
    target_sum = int(input())
    result = two_sum_naive(values, target_sum)
    print(' '.join(map(str, result)) if result else None)
