import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = []
    for var in arr:
        heapq.heappush(heap, var)
    last_node = len(arr)
    last_node_idx = last_node - 1
    ans = 0
    while last_node_idx > 0:
        parent_node = last_node // 2
        parent_node_idx = parent_node - 1
        ans += heap[parent_node_idx]
        last_node = parent_node
        last_node_idx = parent_node_idx
    print(f"#{tc} {ans}")