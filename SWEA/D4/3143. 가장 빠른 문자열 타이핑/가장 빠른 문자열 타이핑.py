T = int(input())

for tc in range(1, T + 1):
    A, B = map(str, input().split())
    current_idx = 0
    typed = 0
    if B in A:
        while current_idx < len(A):
            # 패턴과 동일할 경우
            if A[current_idx:current_idx + len(B)] == B:
                typed += 1
                current_idx += len(B)
            else:
                # 패턴이 최대 문자열의 최대 길이를 초과할 경우
                if len(A) - 1 < current_idx + len(B):
                    typed += len(A) - current_idx
                    break
                else:
                    typed += 1
                    current_idx += 1
        print(f"#{tc} {typed}")
    else:
        print(f"#{tc} {len(A)}")
