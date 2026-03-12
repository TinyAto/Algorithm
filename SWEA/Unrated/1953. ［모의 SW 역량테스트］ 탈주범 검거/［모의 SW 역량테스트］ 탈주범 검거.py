from collections import deque

T = int(input())


def get_dir(type):
    if type == 1:
        return [0, 1, 2, 3]
    elif type == 2:
        return [0, 2]
    elif type == 3:
        return [1, 3]
    elif type == 4:
        return [0, 1]
    elif type == 5:
        return [1, 2]
    elif type == 6:
        return [2, 3]
    elif type == 7:
        return [0, 3]


def is_available(y, x):
    return 0 <= y < N and 0 <= x < M


mapper = {
    (0, 1): 3,
    (-1, 0): 2,
    (0, -1): 1,
    (1, 0): 0,
}


def is_connected(r, c, newr, newc):
    incomming_dir = mapper[(newr - r, newc - c)]
    if incomming_dir in get_dir(arr[newr][newc]):
        return True
    return False


def bfs(r, c, time):
    q = deque()
    q.append((r, c, time))
    visited[r][c] = time
    while q:
        current_r, current_c, newtime = q.popleft()
        for i in get_dir(arr[current_r][current_c]):
            newr = current_r + drs[i]
            newc = current_c + dcs[i]
            # 좌표범위 안이고
            if is_available(newr, newc):
                # 파이프가 있으면서
                if arr[newr][newc]:
                    # 방문하지 않았고
                    if not visited[newr][newc]:
                        # 이전 파이프와 연결되어 있으면
                        if is_connected(current_r, current_c, newr, newc):
                            # 다음회차가 시간 제한 시간 안인지 확인
                            if newtime + 1 <= L:
                                # enqueue
                                q.append((newr, newc, newtime + 1))
                                # 방문체크
                                visited[newr][newc] = newtime + 1


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    bfs(R, C, 1)
    result = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                result += 1
    print(f"#{tc} {result}")
