i = 1000 
while i > 100:
	print(i)
	i /= 2
#b = input ('Введите слово: ')
for j in input('Введите слово: '):
	if j == 'a':
		break
	print(j * 2, end = '')
else:
	print('Буквы а нету в слове')