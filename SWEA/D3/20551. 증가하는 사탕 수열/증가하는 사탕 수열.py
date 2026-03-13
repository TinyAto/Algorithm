T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} ", end='')
    a, b, c = map(int, input().split())
    ans = 0
    if c < 3 or b < 2:
        print(-1)
    else:
        # while b >= c:
        #     b -= 1
        #     ans += 1
        # while a >= b:
        #     a -= 1
        #     ans += 1
        # print(ans)
        if b >= c:
            ans += b - (c - 1)
            b = c - 1
        if a >= b:
            ans += a - (b - 1)
            a = b - 1
        print(ans)
