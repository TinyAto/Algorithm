T = int(input())
for tc in range(1, T + 1):
    dec = float(input())
    binary = '0.'
    digit = 0
    while digit != 13:
        digit += 1
        dec = dec * 2
        if dec >= 1:
            binary += '1'
            dec -= 1
        else:
            binary += '0'

        if int(dec * 100000000) == 0:
            break
    print(f"#{tc} {str(binary)[2:] if digit < 13 else 'overflow'}")
