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
    islands = list(zip(x_cords, y_cords))
    taxrate = float(input()) # E
    visited = [False] * N
    mapper = {}
    for idx, island in enumerate(islands):
        mapper[island] = idx

    pq = []
    heapq.heappush(pq, (0, islands[0]))
    total_cost = 0

    while pq:
        cost, island = heapq.heappop(pq)
        island_idx = mapper[island]

        if visited[island_idx]:
            continue

        visited[island_idx] = True
        total_cost += cost

        for next_island in islands:
            tax = get_tax(taxrate, island, next_island)
            heapq.heappush(pq, (tax, next_island))

    print(f"#{tc} {round(total_cost)}")