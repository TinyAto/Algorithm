# 풀이시작 1510~1539
import sys
from inspect import currentframe, getfile

input_text_flie_name = getfile(currentframe()).split("/")[-1][:-3] + ".txt"
try:
    sys.stdin = open(input_text_flie_name)
except:
    with open(input_text_flie_name, 'w', encoding='utf-8') as f:
        pass
    sys.stdin = open(input_text_flie_name)

T = int(input())

dys = [-1, -1, 0, 1, 1, 1, 0, -1]
dxs = [0, 1, 1, 1, 0, -1, -1, -1]


def is_available(y, x):
    return 0 <= y < N and 0 <= x < N


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hunter_cord = []
    ans = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                hunter_cord.append([i, j])
    for i in range(len(hunter_cord)):
        killed = 0
        for j in range(8):
            hunter = hunter_cord[i][:]
            while True:
                newy = hunter[0] + dys[j]
                newx = hunter[1] + dxs[j]
                if is_available(newy, newx):
                    if arr[newy][newx] == 3:
                        break
                    elif arr[newy][newx] == 2:
                        killed += 1
                    hunter[0] = newy
                    hunter[1] = newx
                else:
                    break
        ans.append(killed)

    print(f"#{tc} {sum(ans)}")