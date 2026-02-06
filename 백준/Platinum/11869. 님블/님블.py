M = int(input())
pos = list(map(int, input().split()))

xor_sum = 0
for p in pos:
    xor_sum ^= p

if xor_sum:
    print("koosaga")
else:
    print("cubelover")