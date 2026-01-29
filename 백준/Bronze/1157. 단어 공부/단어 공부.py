input_str = input().upper()
count_dict = {}
for char in input_str:
    if char not in count_dict:
        count_dict.setdefault(char, 1)
    else:
        count_dict[char] += 1
count_list = list(count_dict.values())
maxval = max(count_list)
count_list.remove(maxval)
if maxval in count_list:
    print("?")
else:
    for key, value in count_dict.items():
        if value == maxval:
            print(key)
