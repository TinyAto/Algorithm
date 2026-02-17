import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
# 상단, 좌측 0패딩 한 배열 생성
solution_arr = [[0] * (N + 1) for _ in range(N + 1)]

# 패딩한 배열으로 이동
for i in range(N):
    for j in range(N):
        solution_arr[i + 1][j + 1] += arr[i][j]
# 1번 행렬 제외한 부분 누적합 구하기
for i in range(1, len(solution_arr)):
    for j in range(1, len(solution_arr[0])):
        solution_arr[i][j] += solution_arr[i - 1][j] + solution_arr[i][j - 1] - solution_arr[i - 1][j - 1]


for m in range(M):
    # x가 행 / y가 열
    x1, y1, x2, y2 = map(int, input().split())
    sum = solution_arr[x2][y2] - solution_arr[x2][y1 - 1] - solution_arr[x1 - 1][y2] + solution_arr[x1 - 1][y1 - 1]
    print(sum)