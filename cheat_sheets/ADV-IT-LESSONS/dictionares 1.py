
input_name = input('''Welcome, user!
You\'r name: ''')

hero = {
    'name': input_name,
    'race': 'Orc',
    'level': 1,
    'health': 100,
    'color': 'green',
    'loc_x': 5,
    'loc_y': 15

}


print(f'Hello, {hero["name"]}! Welcome to our new World of Warcraft.')
print(f'You are {hero["race"]}. ')
print(f'Location X is: {hero["loc_x"]}.')
print(f'Location Y is: {hero["loc_y"]}.')

hero['rank'] = 'Neofit'
print(hero['rank'])

del hero['rank']

hero['loc_x'] += 10
print(hero['loc_x'])

hero['health'] -= 25

if hero['health'] < 80:
    hero['color'] = 'yellow'
    print('Use health potion!')

