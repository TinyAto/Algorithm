from itertools import permutations


def solution(comb):
    pastnode = 0
    used_battery = 0
    for node in comb:
        used_battery += arr[pastnode][node - 1]
        pastnode = node - 1
    used_battery += arr[pastnode][0]
    return used_battery


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dest = list(range(2, N + 1))
    combi = list(permutations(dest, N - 1))
    used_battery = float('inf')
    for comb in combi:
        temp = solution(comb)
        if temp < used_battery:
            used_battery = temp
    print(f"#{i} {used_battery}")
