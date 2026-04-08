from itertools import combinations


def subset_sums(nums):
    result = []
    n = len(nums)

    for r in range(1, n + 1):
        for comb in combinations(nums, r):
            result.append(sum(comb))

    return result


T = int(input())
for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    ppl_count = temp[0]
    height = temp[1]
    temp = list(map(int, input().split()))
    ppl = temp
    subsets = subset_sums(ppl)
    ans = max(subsets)
    for subset in subsets:
        if subset >= height:
            if subset - height < ans:
                ans = subset - height
    print("#{} {}".format(test_case, ans))