numbers = [4,7,2,3,5,6,7,8,2,4]
uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)
