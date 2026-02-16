import sys
from inspect import currentframe, getfile

input_text_flie_name = getfile(currentframe()).split("/")[-1][:-3] + ".txt"
try:
    sys.stdin = open(input_text_flie_name)
except:
    with open(input_text_flie_name, 'w', encoding='utf-8') as f:
        pass
    sys.stdin = open(input_text_flie_name)


def is_available(y, x):
    return 0 <= y < N and 0 <= x < N


T = int(input())
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]
# H 집 / 기지국 A, B, C가 1, 2, 3
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 안테나의 좌표정보 튜플로 저장
    antennas = []
    for i in range(N):
       for j in range(N):
            if arr[i][j] in "ABC":
                antennas.append((i, j))
    # 좌표정보(튜플)하나씩 추출
    for a in antennas:
        antenna = a[:]
        if arr[antenna[0]][antenna[1]] == "A":
            for i in range(4):
                newy = antenna[0] + dys[i]
                newx = antenna[1] + dxs[i]
                if is_available(newy, newx) and arr[newy][newx] == "H":
                    arr[newy][newx] = "X"
        elif arr[antenna[0]][antenna[1]] == "B":
            for j in range(2):
                for i in range(4):
                    newy = antenna[0] + dys[i] * (j+1)
                    newx = antenna[1] + dxs[i] * (j+1)
                    if is_available(newy, newx) and arr[newy][newx] == "H":
                        arr[newy][newx] = "X"
        elif arr[antenna[0]][antenna[1]] == "C":
            for j in range(3):
                for i in range(4):
                    newy = antenna[0] + dys[i] * (j+1)
                    newx = antenna[1] + dxs[i] * (j+1)
                    if is_available(newy, newx) and arr[newy][newx] == "H":
                        arr[newy][newx] = "X"
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "H":
                cnt += 1

    print(f"#{tc} {cnt}")
