T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    pascal = [['1']]
    print(f"#{tc}")
    for i in range(N):
        if i == 0:
            continue
        elif i == 1:
            pascal.append(['1', '1'])
            continue
        else:
            temp = ['1']
            for j in range(i - 1):
                temp.append(str(int(pascal[i - 1][j]) + int(pascal[i - 1][j + 1])))
            temp.append('1')
            pascal.append(temp)
    for line in pascal:
        print(' '.join(line))