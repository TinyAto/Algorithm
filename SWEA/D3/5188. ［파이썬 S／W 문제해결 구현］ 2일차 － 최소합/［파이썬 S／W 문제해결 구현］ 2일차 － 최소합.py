from collections import deque


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = arr[0][0]
    while q:
        current_x, current_y = q.popleft()
        for i in range(2):
            newx, newy = current_x + dxs[i], current_y + dys[i]
            if 0 <= newx < N and 0 <= newy < N:
                temp = visited[current_y][current_x] + arr[newy][newx]
                if temp < visited[newy][newx]:
                    q.append((newy, newx))
                    visited[newy][newx] = visited[current_y][current_x] + arr[newy][newx]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    # 오른쪽, 아래쪽
    dys = [0, 1]
    dxs = [1, 0]
    bfs()
    print(f"#{tc} {visited[N - 1][N - 1]}")
