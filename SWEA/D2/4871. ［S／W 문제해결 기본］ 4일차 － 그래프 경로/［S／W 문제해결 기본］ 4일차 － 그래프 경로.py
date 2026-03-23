def dfs(v):
    # 방문체크
    visited[v] = True
    # 현재 위치가 도착지점인지 체크
    if v == G:
        return True
    for w in adj_lst[v]:
        if not visited[w]:
            if dfs(w):
                return True
    return False


T = int(input())

for tc in range(T):
    # 노드 수, 간선 수 입력
    V, E = map(int, input().split())
    # 인접 리스트 생성
    adj_lst = [[] for _ in range(V + 1)]
    # 방문 리스트 생성
    visited = [False] * (V + 1)
    for i in range(E):
        s, e = map(int, input().split())
        adj_lst[s].append(e)
    S, G = map(int, input().split())
    dfs(S)
    print(f"#{tc + 1} {1 if visited[G] else 0}")
