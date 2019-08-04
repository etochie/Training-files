def summ_cifr_chisla(num):
    print(num)
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum


print(summ_cifr_chisla(2 ** 10))



