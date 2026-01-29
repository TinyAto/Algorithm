N = int(input())
group_count = 0
for i in range(N):
    string = input()
    used = set()
    is_group = True
    for j in range(len(string)):
        if string[j] in used:
            if string[j - 1] == string[j]:
                continue
            else:
                is_group = False
                break
        else:
            used.add(string[j])
    if is_group:
        group_count += 1
print(group_count)