def recur(plus_cnt, minus_cnt, mul_cnt, div_cnt, sum_val, current_idx):
    global max, min
    if plus_cnt == 0 and minus_cnt == 0 and mul_cnt == 0 and div_cnt == 0:
        # TODO : 최대최소 비교
        if max < sum_val:
            max = sum_val
        if min > sum_val:
            min = sum_val
        return
    if plus_cnt > 0:
        recur(plus_cnt - 1, minus_cnt, mul_cnt, div_cnt, sum_val + nums[current_idx], current_idx + 1)
    if minus_cnt > 0:
        recur(plus_cnt, minus_cnt - 1, mul_cnt, div_cnt, sum_val - nums[current_idx], current_idx + 1)
    if mul_cnt > 0:
        recur(plus_cnt, minus_cnt, mul_cnt - 1, div_cnt, sum_val * nums[current_idx], current_idx + 1)
    if div_cnt > 0:
        recur(plus_cnt, minus_cnt, mul_cnt, div_cnt - 1, int(sum_val / nums[current_idx]), current_idx + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    oper = ['+', '-', '*', '/']
    plus, minus, mul, div = map(int, input().split())
    nums = list(map(int, input().split()))
    max = -100000000
    min = 100000000
    recur(plus, minus, mul, div, nums[0], 1)
    print(f"#{tc} {max - min}")