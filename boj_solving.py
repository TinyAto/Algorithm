# https://www.acmicpc.net/problem/2206
import pprint
import sys
from collections import deque

sys.stdin = open("boj_solving.txt")


def is_available(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs(pos):
    q = deque()
    q.append(pos)
    current_y = pos[0]
    current_x = pos[1]
    visited[current_y][current_x] = 1
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
                        # 부수고 이동
                        q.append((newy, newx, 0))
                        # 방문체크
                        # 방문한적 없으면
                        if not visited[newy][newx]:
                            visited[newy][newx] = visited[current_y][current_x] + 1
                            # pprint.pprint(visited)
                        # 방문한 적 있으면
                        else:
                            # 방문체크 배열에 저장된 거리보다 현재 이동 거리가 더 작으면
                            if visited[newy][newx] > visited[current_y][current_x] + 1:
                                visited[newy][newx] = visited[current_y][current_x] + 1
                #                                 pprint.pprint(visited)
                # 길이면
                else:
                    # 방문확인
                    # 방문한적 없으면 enqueue, 방문체크
                    if not visited[newy][newx]:
                        q.append((newy, newx, breakable))
                        visited[newy][newx] = visited[current_y][current_x] + 1
                    #                         pprint.pprint(visited)
                    # 방문한 적 있으면
                    else:
                        # 방문체크 배열에 저장된 거리보다 현재 이동 거리가 더 작으면
                        if visited[newy][newx] > visited[current_y][current_x] + 1:
                            # enqueue, 방문체크
                            q.append((newy, newx, breakable))
                            visited[newy][newx] = visited[current_y][current_x] + 1


#                             pprint.pprint(visited)
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# (y, x, 부술수 있는 횟수)
start_pos = (0, 0, 1)
visited = [[0 for _ in range(M)] for _ in range(N)]

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]
bfs(start_pos)

if visited[N - 1][M - 1]:
    print(visited[N - 1][M - 1])
else:
    print(-1)
