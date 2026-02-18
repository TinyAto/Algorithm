# 7명 뽑는 조합 구하기
def combination(level, combi_temp, n):
    global combi, cnt
    if level == len(ppl):
        if n == len(combi_temp):
            combi.append(combi_temp[:])
            return
        else:
            return
    if n == len(combi_temp):
        combi.append(combi_temp[:])
        return
    else:
        combi_temp.append(ppl[level])
        combination(level + 1, combi_temp, 7)
        combi_temp.pop()
        combination(level + 1, combi_temp, 7)



ppl = [int(input()) for _ in range(9)]
combi = []
cnt = 0
combination(0, [], 7)
for c in combi:
    if sum(c) == 100:
        print(*sorted(c))
        break