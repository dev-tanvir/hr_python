from collections import Counter

n_o_sh = input()
sh_sz = input().split()
sh_sz_dict = [int(x) for x in sh_sz]
shoe_dict = Counter(sh_sz_dict)
cus_num = int(input())
total = 0

for i in range(cus_num):
    (cus_size, sh_price) = map(int, input().split())

    if shoe_dict[cus_size] > 0:
        shoe_dict[cus_size] -= 1
        total += sh_price

print(total)


