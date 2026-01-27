import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    text_n = int(input())
    text_data = input()
    final_string = []
    for char in text_data:
        final_string.append(char)
        if final_string[-3:] == ['f', 'o', 'x']:
            final_string.pop()
            final_string.pop()
            final_string.pop()
    print(len(final_string))