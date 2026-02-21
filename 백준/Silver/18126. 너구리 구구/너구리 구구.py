from collections import deque
def make_adj_lst(lst):
    adj_lst = [[] for _ in range(N + 1)]
    for start, destination, distance in lst:
        adj_lst[start].append((destination, distance))
        adj_lst[destination].append((start, distance))
    return adj_lst


def bfs(room, distance):
    # 방문체크 겸 거리 기록용 배열
    moved_distance = [float("inf")] * (N + 1)
    q = deque()
    # (방 번호, 입구꺼지의 거리)
    q.append((room, distance))
    moved_distance[room] = distance
    while q:
        current_room_num, current_room_distance = q.popleft()
        # 현재 방 번호의 인접 리스트 순회
        for next_room_num, next_room_distance in adj_lst[current_room_num]:
            # 다음 방의 이동거리가 기록되어 있지 않고 큐에 없을 경우(아님)
            # 기록된 다음 방까지의 거리가 현재 방까지 이동한 거리 + 다음 방까지 이동할 거리 보다 큰 경우
            if moved_distance[next_room_num] > next_room_distance + moved_distance[current_room_num]:
                # 다음 방 enqueue
                q.append((next_room_num, next_room_distance))
                # 다음방까지 가는데 이동한 거리 = 다음방 가는데 필요한 거리 + 현재까지 이동한 거리
                moved_distance[next_room_num] = next_room_distance + moved_distance[current_room_num]
    return moved_distance


N = int(input())
adj_info = [list(map(int, input().split())) for _ in range(N - 1)]
# print(adj_info)
# 인접 리스트 만들기(거리 포함), (정점 번호, 거리)형식 튜플로 저장됨
adj_lst = make_adj_lst(adj_info)
# print(adj_lst)
# 이동거리를 저장하는 배열 반환하는 bfs함수
moved = bfs(1, 0)[1:]

print(max(moved))

