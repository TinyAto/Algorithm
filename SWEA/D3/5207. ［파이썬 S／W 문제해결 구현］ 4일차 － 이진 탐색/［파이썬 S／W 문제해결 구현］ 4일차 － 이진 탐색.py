def get_mid(l, r):
    return (l + r) // 2


def binary_search(l, r, target, path):
    while l <= r:
        mid = get_mid(l, r)
        if A[mid] == target:
            return True
        # 중앙값이 타겟값보다 작음(우측 탐색)
        elif A[mid] < target:
            # 초기값이거나 이전에 좌측을 탐색했어야 함
            if path == 'L' or path == '':
                l = mid + 1
                path = 'R'
            else:
                return False
        elif A[mid] > target:
            # 초기값이거나 이전에 우측을 탐색했어야 함
            if path == 'R' or path == '':
                r = mid - 1
                path = 'L'
            else:
                return False
    return False

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    l = 0
    r = N - 1
    ans = 0
    for idx_b in range(M):
        target = B[idx_b]
        result = binary_search(l, r, target, '')
        if result:
            ans += 1
    print(f"#{tc} {ans}")
