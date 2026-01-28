dices = list(map(int, input().split()))
win = 0
dices_set = {dices[0], dices[1], dices[2]}

if len(dices_set) == 1:
    win += 10000 + 1000 * dices_set.pop()
elif len(dices_set) == 2:
    for dice in dices_set:
        if dices.count(dice) == 2:
            win += 1000 + dice * 100
else:
    win += max(dices) * 100

print(win)