T = int(input())

for tc in range(1, T + 1):
    input_string = input()
    top = -1
    stack = []
    print(f"#{tc} ", end='')
    is_right = True
    for char in input_string:
        if char == '(' or char == '{':
            stack.append(char)
            top += 1
            continue
        elif char == ')':
            try:
                compare = stack.pop()
            except:
                is_right = False
                break
            if compare != '(':
                is_right = False
                break
        elif char == '}':
            try:
                compare = stack.pop()
            except:
                is_right = False
                break
            if compare != '{':
                is_right = False
                break
        if not is_right:
            break
    if is_right and not stack:
        print(1)
    else:
        print(0)