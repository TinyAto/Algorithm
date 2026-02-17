import sys
from inspect import currentframe, getfile

input_text_flie_name = getfile(currentframe()).split("/")[-1][:-3] + ".txt"
try:
    sys.stdin = open(input_text_flie_name)
except:
    with open(input_text_flie_name, 'w', encoding='utf-8') as f:
        pass
    sys.stdin = open(input_text_flie_name)

T = int(input())

for tc in range(1, T+1):
    change = int(input())
    n = int(input())
    coin_list = list(map(int, input().split()))
    coin_list.sort()
    coin_dict = {}
    solution = []
    for coin in coin_list:
        coin_dict.setdefault(coin, 0)
    for i in range(len(coin_list)):
        coin_cnt = 1
        coins_except_one = coin_list[:]
        coins_except_one.remove(coin_list[i])
        while True:
            left_change = change - coin_list[i] * coin_cnt
            if left_change <= 0:
                break

