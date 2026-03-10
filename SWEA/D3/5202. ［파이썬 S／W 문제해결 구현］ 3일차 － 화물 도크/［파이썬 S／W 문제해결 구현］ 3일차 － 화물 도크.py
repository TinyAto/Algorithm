def write_timetable(start, end):
    for i in range(start, end):
        timetable[i] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    times = [tuple(map(int, input().split())) for _ in range(N)]
    new_times = []
    for t in times:
        # (시작시간, 끝나는시간, 소요시간)
        new_times.append((t[0], t[1], t[1] - t[0]))
    new_times.sort(key=lambda x: x[2])
    work_nums = list(range(N))
    ans = 0
    timetable = [0] * 25
    for work in work_nums:
        start, end, _ = new_times[work]
        all_checked = True
        for i in range(start, end):
            if timetable[i] == 0:
                continue
            else:
                all_checked = False
                break
        if all_checked:
            write_timetable(start, end)
            ans += 1
    print(f"#{tc} {ans}")