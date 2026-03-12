T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    adj_lst = [tuple(map(int, input().split())) for _ in range(N)]
    max_height = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            if j != i:
                if  ((adj_lst[i][1] - adj_lst[i][0]) - (adj_lst[j][1] - adj_lst[j][0])) != 0:
                    x = (adj_lst[j][0] - adj_lst[i][0]) / ((adj_lst[i][1] - adj_lst[i][0]) - (adj_lst[j][1] - adj_lst[j][0]))
                else:
                    x = adj_lst[j][0] - adj_lst[i][0]
                if 0 < x < 1:
                    ans += 1

    print(f"#{tc} {ans // 2}")
    