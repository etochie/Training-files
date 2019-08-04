def factroial(num):
    if num == 0:
        return 1
    else:
        return num * factroial(num - 1)


def summ_cifr_chisla(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum


print(factroial(100))
print(summ_cifr_chisla(factroial(100)))


