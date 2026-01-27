# 원 방정식
# x^2 + y^2 = r^2
import math
import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # 같은 원(무한대)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 내접 or 외접(접접 1개)
    elif abs(r1 + r2) == distance or abs(r1 - r2) == distance:
        print(1)
    # 만나지 않을 때
    elif abs(r1 + r2) < distance or abs(r1 - r2) > distance:
        print(0)
    else:
        print(2)

