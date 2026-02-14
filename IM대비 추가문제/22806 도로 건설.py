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
    min_height = 5 * N * N
    min_cost = 5 * N * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            height_lst = get_bridge_value(arr, i, j)
            # build_height: 현재 건설 예정인 높이
            # height: 배열 내부 요소의 높이
            for build_height in set(height_lst):
                cost = 0
                for height in height_lst:
                    cost += abs(height - build_height)
                # 기록되어있는 최소 코스트가 현재 코스트보다 크면
                if min_cost > cost:
                    # 최소 코스트, 최소 높이 둘다 업데이트
                    min_cost = cost
                    min_height = build_height
                # 기록되어있는 최소 코스트가 현재 코스트보다 크면
                elif min_cost == cost:
                    # 기록되어있는 최소 높이가 현재 높이보다 크면
                    if min_height > build_height:
                        # 높이 최솟값 업데이트
                        min_height = build_height
    print(f"#{tc + 1} {min_cost} {min_height}")
