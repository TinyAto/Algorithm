import sys
sys.stdin = open("input.txt", "r")

T = int(input())

count = [0, 0]
def fibonacci(n):
    global dynfibo
    global count
    # fibonacci(0)
    if n == 0:
        count[0] += 1
        return 0
    # fibonacci(1)
    elif n == 1:
        count[1] += 1
        return 1
    # fibonacci(2~)
    else:
        # 임시 저장공간에 있을 시 <-- 이때가 문젠데 값이 있을 경우 어떻게?
        # 일단 N번 한번 쫙 돌고 fibonacci(N-1)의 호출 수는 (count[1] - count[0], count[0])인데..
        if dynfibo[n - 1] != 0:

            return dynfibo[n]
        # 임시 저장공간에 없을 시
        else:
            dynfibo[n - 1] = fibonacci(n - 2) + fibonacci(n - 1)
            return fibonacci(n-1) + fibonacci(n-2)
for test_case in range(1, T + 1):
    N = int(input())
    dynfibo = [0] * N
    fibo_N = fibonacci(N)
    print(f"{count[0]} {count[1]}")
    count = [0, 0]