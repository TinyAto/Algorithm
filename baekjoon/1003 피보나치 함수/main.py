import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    zero_count = [1, 0]
    one_count = [0, 1]
    for i in range (2, N + 1):
        zero_count.append(zero_count[i - 1] + zero_count[i - 2])
        one_count.append(one_count[i - 1] + one_count[i - 2])
    print(zero_count[N], one_count[N])