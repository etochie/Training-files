import math

pass_div = int(input('Количество делителей: '))
num = 1
cur_tri = 0
div = []


while len(div) <= pass_div:
    div = []
    cur_tri += num

    for i in range(1, math.ceil(math.sqrt(cur_tri))):
        if cur_tri % i == 0:
            div.append(i)
            div.append(' ')

    num += 1

for j in div:
    print(j, end='')

print('\n' + str(cur_tri))