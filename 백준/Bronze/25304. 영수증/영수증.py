total = int(input())
N = int(input())
sum_of_price = 0
for i in range(N):
    price, count = map(int, input().split())
    sum_of_price += (price * count)
if total == sum_of_price:
    print("Yes")
else:
    print("No")
