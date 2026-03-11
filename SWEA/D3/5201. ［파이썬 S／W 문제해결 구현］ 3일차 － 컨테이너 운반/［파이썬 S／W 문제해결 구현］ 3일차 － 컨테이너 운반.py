T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    ans = 0
    for tr in range(M):
        for cont in range(N):
            if truck[tr] >= container[cont]:
                ans += container[cont]
                container[cont] = float('inf')
                break
    print(f"#{tc} {ans}")
