def is_available(x, y):
    return 0 <= y < N and 0 <= x < M


M, N = map(int, input().split())
seat = int(input())
arr = [[False] * M for _ in range(N)]
cnt = 1
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]
head = 0
# 시작점 index
x_cord = 0
y_cord = N-1
arr[y_cord][x_cord] = True
if seat > N * M:
    print(0)
else:
    for i in range(seat - 1):
        # 도착지 좌표
        newx = x_cord + dxs[head]
        newy = y_cord + dys[head]
        # 도착지 좌표가 좌표평면 밖일 경우
        if not is_available(newx, newy):
            # 회전 후 전진
            head = (head + 1) % 4
            x_cord += dxs[head]
            y_cord += dys[head]
        # 도착지 좌표가 True 일 경우
        elif arr[newy][newx]:
            # 회전 후 전진
            head = (head + 1) % 4
            x_cord += dxs[head]
            y_cord += dys[head]
        else:
            # 그냥 전진
            x_cord += dxs[head]
            y_cord += dys[head]
        arr[y_cord][x_cord] = True
    print(x_cord + 1, N - y_cord)