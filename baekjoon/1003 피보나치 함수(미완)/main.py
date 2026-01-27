import sys
sys.stdin = open("input.txt", "r")

T = int(input())

count_0 = 0
count_1 = 0
def fibonacci(n):
    global count_0
    global count_1
    if (n == 0):
        count_0 += 1
        return 0
    elif (n == 1):
        count_1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for test_case in range(1, T + 1):
    N = int(input())
    fibonacci(N)
    print("{} {}".format(count_0, count_1))
    count_0 = 0
    count_1 = 0