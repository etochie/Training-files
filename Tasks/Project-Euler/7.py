import math


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

p=5
s=[2,3]
while True:
    if is_prime(p):
        s.append(p)
    if len(s) == 10001:
        break
    p+=2

print(s)
print(f'Result: {s[-1]}')
