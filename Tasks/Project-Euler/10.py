import math

p = []


def prime(num):
    if num < 2:
        return False
    if num == 2:
        return True

    i = 2
    limit = math.ceil(math.sqrt(num))

    while i <= limit:
        if num % i == 0:
            return False
        i += 1
    return True


for j in range(2000000):
    if prime(j):
        p.append(j)

print(p)
print(sum(p))
