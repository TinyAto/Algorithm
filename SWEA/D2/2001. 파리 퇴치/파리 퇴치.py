T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    killed = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill = 0
            for a in range(M):
                for b in range(M):
                    temp = arr[i + a][j + b]
                    kill += temp
            killed.append(kill)
    print(f"#{tc} {max(killed)}")