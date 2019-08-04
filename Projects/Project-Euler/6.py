import math

sum1 = 0

for i in range(1,101):
    sum1 += i ** 2

sum2 = sum(range(1,101)) ** 2

print(sum1)
print(sum2)

result = sum2 - sum1
print(result)