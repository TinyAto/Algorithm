# A형 1일차 과제 1번(완료)
import sys

sys.stdin = open("input.txt")
N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x_cord, y_cord = 0, 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
mapper = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
time_elapsed = 0
for i in range(N):
    for j in range(dist[i]):
        time_elapsed += 1
        x_cord, y_cord = x_cord + dxs[mapper[dir[i]]], y_cord + dys[mapper[dir[i]]]
        if x_cord == 0 and y_cord == 0:
            break
    if x_cord == 0 and y_cord == 0:
        break
print(time_elapsed if x_cord == 0 and y_cord == 0 else '-1')
