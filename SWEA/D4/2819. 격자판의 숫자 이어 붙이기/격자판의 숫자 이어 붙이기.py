def is_available(y, x):
    return 0 <= y < N and 0 <= x < N


def dfs(y, x, path):
    if len(path) == 7:
        pathstr = ''.join(map(str, path))
        results.add(pathstr)
        return
    for i in range(4):
        newy = y + dys[i]
        newx = x + dxs[i]
        if is_available(newy, newx):
            path.append(arr[newy][newx])
            dfs(newy, newx, path)
            path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]
    results = set()
    for i in range(N):
        for j in range(N):
            dfs(i, j, [arr[i][j]])
    print(f"#{tc} {len(results)}")
