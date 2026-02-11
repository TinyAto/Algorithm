def my_len(lis):
    l = 0
    for _ in lis:
        l += 1
    return l


def my_maxwithidx_reverse(lis):
    idx = my_len(lis) - 1
    maxval = lis[idx]
    for i in range(idx, -1, -1):
        if maxval < lis[i]:
            maxval = lis[i]
            idx = i
    return maxval, idx


def in_range(y, x):
    return 0 <= y < 100 and 0 <= x < 100


for tc in range(10):
    _ = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    _, idx = my_maxwithidx_reverse(arr[99])
    current_idx = [99, idx]  # y, x
    # 밑에서부터 거슬러 올라감
    head = 1
    while current_idx[0] != 0:
        # 위로 올라가는거 가장 나중에
        # if arr[current_idx[0] - 1][current_idx[1]] == 1:
        #     current_idx = [current_idx[0] - 1, current_idx[1]]
        # 왼쪽 검사
        if current_idx[0] == 67:
            pass
        if in_range(current_idx[0], current_idx[1] - 1) and arr[current_idx[0]][current_idx[1] - 1] == 1:
            while in_range(current_idx[0], current_idx[1] - 1) and arr[current_idx[0]][current_idx[1] - 1] == 1:
                current_idx[1] -= 1
            if in_range(*current_idx):
                current_idx[0] -= 1
        # 오른쪽 검사
        elif in_range(current_idx[0], current_idx[1] + 1) and arr[current_idx[0]][current_idx[1] + 1] == 1:
            while in_range(current_idx[0], current_idx[1] + 1) and arr[current_idx[0]][current_idx[1] + 1] == 1:
                current_idx[1] += 1
            if in_range(*current_idx):
                current_idx[0] -= 1
        # 아니면 직진
        else:
            current_idx = [current_idx[0] - 1, current_idx[1]]
    print(f"#{tc+1} {current_idx[1]}")