from collections import deque

def is_available(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs(pos):
    q = deque()
    q.append(pos)
    current_y = pos[0]
    current_x = pos[1]
    visited[pos[2]][current_y][current_x]= 1
    while q:
        current_y, current_x, breakable = q.popleft()
        for i in range(4):
            newx = current_x + dxs[i]
            newy = current_y + dys[i]
            # 좌표범위 검사
            if is_available(newy, newx):
                # 벽이면
                if arr[newy][newx]:
                    # 부술수 있는지 확인
                    if breakable:
                        if not visited[breakable][newy][newx]:
                            # 부수고 이동
                            q.append((newy, newx, 0))
                            # 방문체크
                            visited[0][newy][newx] = visited[breakable][current_y][current_x] + 1
                # 길이면
                else:
                    if not visited[breakable][newy][newx]:
                        # 방문체크
                        q.append((newy, newx, breakable))
                        visited[breakable][newy][newx] = visited[breakable][current_y][current_x] + 1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# (y, x, 부술수 있는 횟수)
start_pos = (0, 0, 1)
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]
bfs(start_pos)

wall_breaked =visited[0][N - 1][M - 1]
wall_not_breaked =visited[1][N - 1][M - 1]

if wall_breaked or wall_not_breaked:
    if wall_breaked == 0:
        print(wall_not_breaked)
    elif wall_not_breaked == 0:
        print(wall_breaked)
    else:
        print(wall_breaked if wall_breaked < wall_not_breaked else wall_not_breaked)
else:
    print(-1)
