import sys
from inspect import currentframe, getfile
from pkgutil import resolve_name

input_text_flie_name = getfile(currentframe()).split("/")[-1][:-3] + ".txt"
try:
    sys.stdin = open(input_text_flie_name)
except:
    with open(input_text_flie_name, 'w', encoding='utf-8') as f:
        pass
    sys.stdin = open(input_text_flie_name)

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    list_of_sum = []
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            sum_of_value = 0
            # 상단 행
            sum_of_value += sum(arr[i][j:j + K])
            # 하단 행
            sum_of_value += sum(arr[i + K - 1][j:j + K])
            # 중간에 끼인 열
            for y in range(i + 1, i + K - 1):
                for x in range(j, j + K, K - 1):
                    sum_of_value += arr[y][x]
            list_of_sum.append(sum_of_value)
    print(f"#{tc} {max(list_of_sum)}")