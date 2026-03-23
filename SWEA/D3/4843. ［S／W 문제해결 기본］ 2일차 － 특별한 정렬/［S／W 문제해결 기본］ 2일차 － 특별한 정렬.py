T = int(input())


def selection_sort(arr, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, n)
    result = []
    for i in range(n // 2):
        result.append(arr[-(i + 1)])
        result.append(arr[i])
    if n % 2 != 0:
        result.append(arr[(n // 2)])

    print(f"#{tc} ", end='')
    for i in range(10):
        print(f"{result[i]} ", end='')
    print()