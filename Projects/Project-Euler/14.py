def collatz_seq(num):
    res = [num]
    while True:
        if num % 2 == 0:
            num = num / 2
            res.append(num)
        elif num % 2 != 0:
            num = (num * 3) + 1
            res.append(num)
        if num == 1:
            break
    return len(res)


def eul_14(start, stop):
    max = 0
    maxi = 0
    for i in range(start, stop + 1):
        last = collatz_seq(i)
        if last > max:
            max, maxi = last, i
    return max, maxi


print('Euler 14: ' + str(eul_14(1, 1000000)))









