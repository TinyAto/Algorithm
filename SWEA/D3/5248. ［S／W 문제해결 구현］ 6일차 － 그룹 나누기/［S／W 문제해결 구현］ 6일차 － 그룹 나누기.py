'''
# DFS 풀이법
def dfs(v):
    visited[v] = 1
    for w in adj_lst[v]:
        if visited[w] == 0:
            dfs(w)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    adj_lst = [[] for _ in range(N + 1)]  # 인접리스트
    visited = [0] * (N + 1)
    for i in range(M):
        s, e = temp[2 * i], temp[2 * i + 1]
        adj_lst[s].append(e)
        adj_lst[e].append(s)

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')


T = int(input())


def find_set(x):
    if parent[x] != x:
        return find_set(parent[x])
    else:
        return x
'''

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
