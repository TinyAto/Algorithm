T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [0] * (K + 1)

    for V, C in items:
        for w in range(K, V - 1, -1):
            if dp[w - V] + C > dp[w]:
                dp[w] = dp[w - V] + C

    print(f"#{tc} {dp[K]}")
