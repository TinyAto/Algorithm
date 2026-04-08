import heapq

def get_tax(taxrate, island1, island2):
    if taxrate == 0:
        return 0
    else:
        x1, y1 = island1
        x2, y2 = island2
        return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) * taxrate


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x_cords = list(map(int, input().split()))
    y_cords = list(map(int, input().split()))
    taxrate = float(input()) # E
    visited = [False] * N

    pq = []
    heapq.heappush(pq, [0, 0])
    total_cost = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        total_cost += cost

        for node_idx in range(N):
            next_island = (x_cords[node_idx], y_cords[node_idx])
            tax = get_tax(taxrate, (x_cords[node], y_cords[node]), next_island)
            heapq.heappush(pq, (tax, node_idx))

    print(f"#{tc} {round(total_cost)}")