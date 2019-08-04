

hero = {
    'name': 'Klark',
    'race': 'Orc',
    'level': 1,
    'health': 100,
    'color': 'green',
    'loc_x': 5,
    'loc_y': 15

}

all_heroes = []

for x in range(10):
    all_heroes.append(hero.copy())
    #.copy создает КОПИИ hero в массиве all_heroes (можно менять по отдельности)

all_heroes[2]['race'] = 'Human'

for her in all_heroes:
    print(her)




