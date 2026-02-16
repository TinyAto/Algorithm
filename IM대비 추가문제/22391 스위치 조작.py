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

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = list(map(int, input().split()))
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != ans[i]:
            for j in range(i, i + len(arr[i:])):
                arr[j] = int(not(arr[j]))
            cnt += 1
    print(f"#{tc} {cnt}")