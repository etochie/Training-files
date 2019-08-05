import math


def is_pali(num):
    stnum = str(num)
    r_num = int(stnum[::-1])
    if r_num == num:
        return True



list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i*j
        if is_pali(a):
            list.append(a)
print(list)
print(max(list))


























