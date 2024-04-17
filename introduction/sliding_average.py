def sliding_average(values: list, window: int) -> list:
    result = []
    current_sum = sum(values[:window])
    result.append(current_sum/window)

    for i in range(len(values) - window):
        current_sum -= values[i]
        current_sum += values[i+window]
        result.append(current_sum/window)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    window = int(input())
    result = sliding_average(arr, window)
    print(' '.join(map(str, result)))