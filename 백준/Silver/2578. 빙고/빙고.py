arr = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]


def check_row():
    cnt = 0
    for var in arr:
        if set(var) == {0}:
            cnt += 1
    return cnt


def check_column():
    cnt = 0
    for i in range(5):
        col = []
        for j in range(5):
            col.append(arr[j][i])
        if set(col) == {0}:
            cnt += 1
    return cnt


def check_cross():
    cnt = 0
    cross = []
    for i in range(5):
        cross.append(arr[i][i])
    if set(cross) == {0}:
        cnt += 1
    cross = []
    for i in range(5):
        cross.append(arr[i][4-i])
    if set(cross) == {0}:
        cnt += 1
    return cnt

bingo = False
for i in range(5):
    for j in range(5):
        now_calling = call[i][j]
        for var in arr:
            if now_calling in var:
                idx = var.index(now_calling)
                var[idx] = 0
                break
        if i > 1:
            bingo_count = 0
            bingo_count += check_row()
            bingo_count += check_column()
            bingo_count += check_cross()
            if bingo_count >= 3:
                bingo = True
                print(5 * i + j + 1)
                break
    if bingo:
        break