# https://www.acmicpc.net/problem/1022
import sys
sys.stdin = open("input.txt", "r")

r1, c1, r2, c2 = map(int, input().split())
# 정사각현 한 변의 길이는 r2 - r1 + 1
# 자릿수 공백으로 체우기(n자리) print(f"{num:nd}")
# 자릿수 0으로 체우기(n자리) print(f"{num:0nd}")
