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

if __name__ == "__main__":
    from basic_input import basic_input
    import sys

    sys.stdin = basic_input()
