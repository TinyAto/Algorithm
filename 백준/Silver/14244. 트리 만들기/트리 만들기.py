n, m = map(int, input().split())
adj_lst = [[] for _ in range(n)]
adj_lst[0] = [1]
for i in range(m - 1):
    adj_lst[1].append(2 + i)
current_v = m
for i in range(current_v, n - 1):
    adj_lst[i].append(i + 1)

for i in range(len(adj_lst)):
    adj = adj_lst[i]
    for a in adj:
        print(i, a)