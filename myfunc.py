def basic_input():
    import sys, os, inspect
    # 호출한 파일의 스택 프레임을 가져옵니다.
    # index 1이 현재 함수를 호출한 바로 이전 단계를 가리킵니다.
    frame = inspect.stack()[1]

    # 해당 프레임에서 파일 경로를 추출합니다.
    caller_path = frame.filename

    # 파일명만 깔끔하게 추출
    caller_name = os.path.basename(caller_path)

    # print(f"나를 호출한 파일은 바로: {caller_name}")
    input_text_flie_name = caller_name[:-3] + ".txt"
    try:
        textfile = open(input_text_flie_name)
    except:
        with open(input_text_flie_name, 'w', encoding='utf-8') as f:
            pass
        textfile = open(input_text_flie_name)
    return textfile


def my_len(lis):
    l = 0
    for _ in lis:
        l += 1
    return l


def my_sum(lis):
    sum_of_lis = 0
    for l in lis:
        sum_of_lis += l
    return sum_of_lis


def my_max(lis):
    maxval = lis[0]
    for l in lis:
        if maxval < l:
            maxval = l
    return maxval


def my_maxwithidx_reverse(lis):
    idx = my_len(lis) - 1
    maxval = lis[idx]
    for i in range(idx, -1, -1):
        if maxval < lis[i]:
            maxval = lis[i]
            idx = i
    return maxval, idx

def my_minwithidx(lis):
    idx = 0
    minval = lis[idx]
    for i in range(my_len(lis)):
        if minval > lis[i]:
            minval = lis[i]
            idx = i
    return minval, idx