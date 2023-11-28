import os
import sys
import string
from pprint import pprint

mapNames = {
    'airfield': 'Аэродром',
    'asia_great_wall': 'Граница империии',
    'asia_miao': 'Жемчужная река',
    'canada_a': 'Тихий берег',
    'caucasus': 'Перевал',
    'cliff': 'Утес',
    'czech': 'Промзона',
    'czech_hw22': 'Промзона Halloween 2022',
    'dday': 'Оверлорд',
    'desert': 'Песчаная река',
    'eiffel_tower_ctf': 'Париж',
    'el_hallouf': 'Эль-Халлуф',
    'ensk': 'Энск',
    'epic_random_valley': 'Небельбург',
    'erlenberg': 'Эрленберг',
    'fishing_bay': 'Рыбатская бухта',
    'fjord': 'Фьорды',
    'germany': 'Берлин',
    'hills': 'Рудники',
    'himmelsdorf': 'Химмельсдорф',
    'japort': 'Старая гавань',
    'karelia': 'Карелия',
    'lakeville': 'Ласвилль',
    'last_frontier_v': 'Застава',
    'lost_city_ctf': 'Затерянный город',
    'lost_paradise_v': 'Устричный залив',
    'malinovka': 'Малиновка',
    'mannerheim_line': 'Линия Маннергейма',
    'minsk': 'Минск',
    'monastery': 'Монастырь',
    'munchen': 'Уайдпарк',
    'murovanka': 'Мурованка',
    'murovanka_hw22': 'Мурованка Halloween 2022',
    'north_america': 'Хайвей',
    'poland': 'Студзянки',
    'poland_hw22': 'Студзянки Halloween 2022',
    'prohorovka': 'Прохоровка',
    'redshire': 'Редшир',
    'ruinberg': 'Руинберг',
    'ruinberg_hw22': 'Руинберг Halloween 2022',
    'siegfried_line': 'Линия зигфрида',
    'stalingrad': 'Сталинград',
    'steppes': 'Степи',
    'sweden': 'Штиль',
    'tundra': 'Тундра',
    'westfeld': 'Вестфилд',
}

files = []
cwd = os.getcwd()
current_file = sys.argv[0].split('\\')[-1]
for f in os.listdir(cwd):
    if os.path.isfile(os.path.join(cwd, f)):
        if current_file in f:
            continue
        files.append(f)

data = []

for file in files:
    f = file.replace('.wotreplay', '').split('_')

    date = f[0]
    time = f'{f[1][0:2]}:{f[1][2:4]}'
    country = f[2]
    max_index = None
    for i in range(1, len(f)):
        if f[-i][0] in string.digits:
            max_index = i
            break
    map_name = '_'.join(f[-max_index + 1:])

    data.append({
        'date': date,
        'time': time,
        'country': country,
        'map': map_name
    })

dates = set(d.split('_')[0] for d in files)

split_files = [f.replace('.wotreplay', '').split('_') for f in files]

maps = set(m['map'] for m in data)

total = {}

for d in dates:
    total[d] = {}

for file in data:
    d = file['date']
    m = file['map']
    mn = mapNames[m] if m in mapNames else m
    if mn in total[d]:
        total[d][mn] += 1
    else:
        total[d][mn] = 1

if __name__ == '__main__':
    pprint(total)
