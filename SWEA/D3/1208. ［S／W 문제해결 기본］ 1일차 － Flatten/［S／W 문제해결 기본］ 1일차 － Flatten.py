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

def my_minwithidx(lis):
    idx = 0
    minval = lis[idx]
    for i in range(my_len(lis)):
        if minval > lis[i]:
            minval = lis[i]
            idx = i
    return minval, idx


for tc in range(1, 11):
    dump_limit = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump_limit):
        if i == 824:
            a =1
        maxval, idx_max = my_maxwithidx_reverse(arr)
        minval, idx_min = my_minwithidx(arr)
        if maxval - minval == 0 or maxval - minval == 1:
            break
        arr[idx_max] -= 1
        arr[idx_min] += 1
    maxval, _ = my_maxwithidx_reverse(arr)
    minval, _ = my_minwithidx(arr)
    print(f"#{tc} {maxval  - minval}")