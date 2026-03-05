from collections import deque
T = int(input())
mapper_hextobin = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111",
}
mapper = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9,
}

def change_to_bin():
    new_arr = []
    for i in range(N):
        temp = ''
        for j in range(M):
            temp += mapper_hextobin[arr[i][j]]
        new_arr.append(temp)
    return new_arr


def find_encrypted_code(line):
    # 오른쪽 끝 자리 1로 맞추기
    line = list(line)
    while line[-1] != '1':
        line.pop()
    line = ''.join(line)
    # 비밀번호가 몇배수인지 찾기 위해 끝 한자리 찾기
    password = ''
    past_value = '1'
    cnt = 0
    password_ratio = deque()
    for i in range(len(line) - 1, -1, -1):
        current_value = line[i]
        if current_value == past_value:
            cnt += 1
        else:
            password_ratio.appendleft(cnt)
            past_value = current_value
            cnt = 1
            if len(password_ratio) > 4:
                password = list(password_ratio)[1:]
        if password:
            break
    # 비밀번호가 몇배수인지 계산
    password_length = (sum(list(password)) // 7) * basic_password_length
    rest = line[:len(line) - password_length]
    password = line[len(line) - password_length:]

    return rest, password


def get_crypt_ratio(encrypted_words):
    result = []
    for current_words in encrypted_words:
        password = []
        cnt = 0
        password_ratio = deque()
        past_value = current_words[0]
        ratio = len(current_words) // basic_password_length
        for current_value in current_words:
            if current_value == past_value:
                cnt += 1
            else:
                password_ratio.append(str(cnt //  ratio))
                past_value = current_value
                cnt = 1
                if len(password_ratio) > 4:
                    password.append(list(password_ratio)[:-1])
                    for i in range(4):
                        password_ratio.popleft()
        password_ratio.append(str(cnt // ratio))
        password.append(list(password_ratio))
        result.append(password[:])
    return result


def is_legit(password):
    flag = True
    odd = 0
    even = 0
    # 홀수자리(시작 1부터) 합
    for i in range(0, 7, 2):
        odd += password[i]
    # 짝수자리(시작 1부터) 합
    for i in range(1, 7, 2):
        even += password[i]
    if ((odd * 3) + even + password[-1]) % 10 != 0:
        flag = False
    return flag



for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    basic_password_length = 56
    encrypted_words = []
    result_sum = 0
    # 16진수 2진수로 변경
    arr_bin = change_to_bin()
    # 암호문 찾기
    for line in arr_bin:
        rest = line
        while set(rest) != {'0'}:
            rest, encrypted_word = find_encrypted_code(rest)
            if encrypted_word not in encrypted_words:
                encrypted_words.append(encrypted_word)
    # 암호문 비율화
    encrypted_words = get_crypt_ratio(encrypted_words)
    # 비율화된 암호문 한줄씩 꺼내기
    for encrypted in encrypted_words:
        password = []
        for enc in encrypted:
            key = ''
            for var in enc:
                key += var
            password.append(mapper[key])
        # password 검증
        flag = is_legit(password)
        if flag:
            result_sum += sum(password)
    print(f"#{tc} {result_sum}")