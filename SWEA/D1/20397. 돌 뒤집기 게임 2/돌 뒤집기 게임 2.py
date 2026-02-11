T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    list_i = []
    list_j = []
    for i in range(M):
        temp = input().split()
        list_i.append(int(temp[0]) - 1)
        list_j.append(int(temp[1]))
    for j in range(len(list_j)):
        for k in range(1, list_j[j] + 1):
            if 0 <= list_i[j] - k < N and 0 <= list_i[j] + k < N:
                if arr[list_i[j] - k] == arr[list_i[j] + k]:
                    arr[list_i[j] - k] = 0 if arr[list_i[j] - k] == 1 else 1
                    arr[list_i[j] + k] = 0 if arr[list_i[j] + k] == 1 else 1
            else:
                break
    print(f"#{tc + 1} ", end='')
    print(*arr)