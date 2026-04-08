
T = int(input())


def find_set(x):
    if parent[x] != x:
        return find_set(parent[x])
    else:
        return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    parent[y] = x


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    parent = list(x for x in range(N + 1))
    for i in range(M):
        x, y = numbers[i * 2], numbers[i * 2 + 1]
        union(x, y)
    cnt = 0
    for i in range(1, N + 1):
        if parent[i] == i:
            cnt += 1
    print(f"#{tc} {cnt}")
