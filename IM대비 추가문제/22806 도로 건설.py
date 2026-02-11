import sys
from inspect import currentframe, getfile

input_text_flie_name = getfile(currentframe()).split("/")[-1][:-3] + ".txt"
try:
    sys.stdin = open(input_text_flie_name)
except:
    with open(input_text_flie_name, 'w', encoding='utf-8') as f:
        pass
    sys.stdin = open(input_text_flie_name)


def get_bridge_value(arr, i, j):
    result = arr[i][:]
    for k in range(N):
        if k != i:
            result.append(arr[k][j])
    return result


T = int(input())
for tc in range(T):
    N = int(input())
    min_height = 20*20*4
    min_cost = 20*20*4
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cost = 0
            height_lst = get_bridge_value(arr, i, j)
            for build_height in set(height_lst):
                for height in height_lst:
                    cost += abs(height - build_height)
                if min_cost >= cost:
                    if min_height >= build_height:
                        min_cost = cost
                        min_height = build_height
    print(f"#{tc+1} {min_cost} {min_height}")