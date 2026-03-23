def find_page(p, key):
     start = 1
     end = p
     count = 0
     while start <= end:
        center = (start + end) // 2
        if center == key:
            return count
        else:
            if center < key:
                start = center
                count += 1
            else:
                end = center
                count += 1
     return None


T = int(input())

for tc in range(1, T + 1):
    p, a, b = map(int, input().split())

    a_try = find_page(p, a)
    b_try = find_page(p, b)

    if a_try > b_try:
        print(f"#{tc} B")
    elif a_try < b_try:
        print(f"#{tc} A")
    elif a_try == b_try:
        print(f"#{tc} 0")