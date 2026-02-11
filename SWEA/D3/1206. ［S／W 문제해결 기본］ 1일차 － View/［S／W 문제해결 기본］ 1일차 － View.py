def my_max(arr):
    max = arr[0]
    for val in arr:
        if max < val:
            max = val
    return max

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            neighbor = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
            cnt += arr[i] - my_max(neighbor)
    print(f"#{tc+1} {cnt}")
