import math

x = 0
total = [1, 2]

while max(total) < 4000000:
    start = (total[x] + total[x+1])
    total.append(start)
    x += 1


print(total)

total_chetnie = []
for number in total:
    if number % 2 == 0:
        total_chetnie.append(number)
print(total_chetnie)
answer = sum(total_chetnie)
print(answer)






