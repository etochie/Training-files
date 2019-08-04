weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
#upper() - переводит все что ввели в input
#в верхний регистр = не нужно морочиться с 'L/K' or 'l/k'
    print(f"You'r weight is {weight * 0.45} in kg's")
elif unit.upper() == 'K':
    print(f"You'r weight is {weight * 2.2} in lbs")
else:
    print('Error')