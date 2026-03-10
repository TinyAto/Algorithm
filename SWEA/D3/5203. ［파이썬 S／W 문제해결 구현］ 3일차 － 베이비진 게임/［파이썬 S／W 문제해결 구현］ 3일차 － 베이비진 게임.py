def check_run(hand):
    hand.sort()
    # 중복 숫자가 있을 수 있으므로 set으로 중복 제거 후 연속성 확인
    unique_hand = sorted(list(set(hand)))
    for i in range(len(unique_hand) - 2):
        if unique_hand[i] + 1 == unique_hand[i + 1] and unique_hand[i + 1] + 1 == unique_hand[i + 2]:
            return True
    return False


def check_triplet(hand):
    # 숫자의 개수를 세어서 3개 이상인 것이 있는지 확인
    counts = [0] * 10
    for card in hand:
        counts[card] += 1
        if counts[card] >= 3:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    p1_cards = []
    p2_cards = []
    winner = 0

    for i in range(len(arr)):
        # 짝수 인덱스는 플레이어 1, 홀수 인덱스는 플레이어 2
        if i % 2 == 0:
            p1_cards.append(arr[i])
            # 카드가 3장 이상일 때부터 체크
            if len(p1_cards) >= 3:
                if check_run(p1_cards) or check_triplet(p1_cards):
                    winner = 1
                    break
        else:
            p2_cards.append(arr[i])
            if len(p2_cards) >= 3:
                if check_run(p2_cards) or check_triplet(p2_cards):
                    winner = 2
                    break

    print(f"#{tc} {winner}")