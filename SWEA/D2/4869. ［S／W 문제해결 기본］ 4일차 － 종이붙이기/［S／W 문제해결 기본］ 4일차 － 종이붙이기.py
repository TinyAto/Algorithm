T = int(input())


def solution(N):
    if N <= 1:
        return 1
    if memo[N] != 0:
        return memo[N]
    memo[N] = solution(N - 1) + 2 * solution(N - 2)
    return memo[N]


for tc in range(T):
    N = int(input()) // 10
    memo = [0] * (N + 1)
    ans = solution(N)
    print(f"#{tc + 1} {ans}")