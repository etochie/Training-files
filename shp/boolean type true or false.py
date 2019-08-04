is_hot = False
is_cold = False

if is_hot:
    print("Сегодня жарко!")
    print("Пейте больше воды.")
elif is_cold:
    print('Сегодня холодно!')
    print('Одевайтесь теплее.')
else:
    print('Сегодня чудесный день!')
print('Наслаждайтесь!')


###Пример с стоимостью и первоначальным взносом###

price = 1000000
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Price: ${price}')
print(f"You'r down payment: ${down_payment}")