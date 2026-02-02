# # https://www.acmicpc.net/problem/1022
# import sys
# sys.stdin = open("input.txt", "r")
#
# # r1, c1, r2, c2 = map(int, input().split())
# # 정사각현 한 변의 길이는 r2 - r1 + 1
# # 자릿수 공백으로 체우기(n자리) print(f"{num:nd}")
# # 자릿수 0으로 체우기(n자리) print(f"{num:0nd}")
from math import *
import sys
sys.stdin = open("input.txt")
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZtxkCpquDPHBIQE&categoryId=AZtxkCpquDPHBIQE&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
T = int(input())
for tc in range(1, T+1):
    S, P = map(int, input().split())
    if ((S + sqrt(abs(S ** 2 - 4 * P))) / 2):
        print("YES")
    else:
        print("NO")