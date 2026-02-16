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

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    can_split = False
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            upperside = arr[:i]
            lowerside = arr[i:]
            sum_UL = 0
            sum_UR = 0
            sum_DL = 0
            sum_DR = 0
            for k in range(len(upperside)):
                sum_UL += sum(upperside[k][:j])
                sum_UR += sum(upperside[k][j:])
            for k in range(len(lowerside)):
                sum_DL += sum(lowerside[k][:j])
                sum_DR += sum(lowerside[k][j:])
            if sum_UL == sum_UR == sum_DL == sum_DR:
               can_split = True
               break
        if can_split:
            break
    print(f"#{tc} {int(can_split)}")