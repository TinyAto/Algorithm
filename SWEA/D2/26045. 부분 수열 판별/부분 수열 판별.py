T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    check = [0] * M
    checking_idx = 0
    for a in A:
        if a == B[checking_idx]:
            check[checking_idx] = 1
            checking_idx += 1
            if checking_idx == len(B):
                break
    if len(set(check)) == 1:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
