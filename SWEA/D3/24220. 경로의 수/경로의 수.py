def dfs(node, trace):
    global route_cnt
    if node == G:
        trace.append(node)
        # print(trace)
        route_cnt += 1
        return
    elif len(trace) == E:
        return
    for adj_node in adj_lst[node]:
        if not visited[adj_node]:
            visited[adj_node] = True
            dfs(adj_node, trace + [node])
            visited[adj_node] = False


T = int(input())
for tc in range(1, T + 1):
    route_cnt = 0
    N, E = map(int, input().split())
    adj = list(map(int, input().split()))
    adj_lst = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    S, G = map(int, input().split())
    for i in range(0, len(adj), 2):
        adj_lst[adj[i]].append(adj[i + 1])
    visited[S] = True
    dfs(S,[])
    print(f"#{tc} {route_cnt}")