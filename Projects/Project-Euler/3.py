def factor(num):
    result = []
    if num == 2:
        result.append(num)
    for i in range(3, int(num ** 0.5), 2):
        if num % i == 0:
            if len(factor(i)) == 0:
                result.append(i)
    return result


print(factor(600851475143))


















