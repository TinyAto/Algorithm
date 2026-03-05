T = int(input())
mapper = {'0001101': '0',
          '0011001': '1',
          '0010011': '2',
          '0111101': '3',
          '0100011': '4',
          '0110001': '5',
          '0101111': '6',
          '0111011': '7',
          '0110111': '8',
          '0001011': '9',
          }
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    encrypted_word = []
    for line in arr:
        for i in range(M - 1, -1, -1):
            if line[i] != 0:
                encrypted_word = line[i - 55: i + 1]
                break
        if encrypted_word:
            break
    passcode = ''
    for i in range(0, 56, 7):
        part = encrypted_word[i:i + 7]
        temp = ''
        for j in range(7):
            temp += str(part[j])
        passcode += str(mapper[temp])
    # 짝수 자리수
    even = 0
    for i in range(0, 8, 2):
        even += int(passcode[i])
    even *= 3

    # 홀수 자리수
    odd = 0
    for i in range(1, 8, 2):
        odd += int(passcode[i])
    print(f"#{tc} ", end='')
    # 10의 배수인지 확인
    result = odd + even
    if result % 10 == 0:
        ans = 0
        for var in passcode:
            ans += int(var)
        print(ans)
    else:
        print(0)
