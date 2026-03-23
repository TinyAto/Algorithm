T = int(input())

for tc in range(1, T + 1):
    init_str = input()
    final_str = []
    last_deleted_word = ''
    top = -1
    for i in range(len(init_str)):
        final_str.append(init_str[i])
        top += 1
        if top - 1 >= 0 and final_str[top - 1] == final_str[top]:
            final_str.pop()
            final_str.pop()
            top -= 2
    print(f"#{tc} {len(final_str)}")