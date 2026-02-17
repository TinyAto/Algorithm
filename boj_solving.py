# https://www.acmicpc.net/problem/1244
import sys
sys.stdin = open("boj_solving.txt")
# 스위치 수 N
N = int(input())
# 스위치
switches = list(map(int, input().split()))
# 학생 수 M
students = []
M = int(input())
for _ in range(M):
    students.append(list(map(int, input().split())))

for student in students:
    # 스위치 인덱스
    switch_idx = student[1] - 1
    # 남학생
    if student[0] == 1:
        for i in range(1, N + 1):
            if i % (switch_idx + 1) == 0:
                switches[i - 1] = int(not switches[i - 1])
    # 여학생
    elif student[0] == 2:
        switches[switch_idx] = int(not switches[switch_idx])
        offset = 1
        while True:
            if 0 <= switch_idx - offset < N and 0 <= switch_idx + offset < N:
                if switches[switch_idx - offset] == switches[switch_idx + offset]:
                    offset += 1
                else:
                    break
            else:
                break
        offset -= 1
        for i in range(1, offset + 1):
            switches[switch_idx - i] = int(not switches[switch_idx - i])
            switches[switch_idx + i] = int(not switches[switch_idx + i])
print(*switches, end='')