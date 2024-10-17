from django.shortcuts import render, redirect
from .models import Heroes
from .forms import *
from bs4 import BeautifulSoup
import requests

a = []
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('last_pick')

    else:
        form = UserForm()
    return render(request, 'main/index.html',
                  {'form': form})


def last_pick(request):
    heroes = Heroes.objects.order_by('-id')[0]
    h = picker([heroes.first_hero, heroes.second_hero, heroes.third_hero, heroes.fourth_hero])

    return render(request, 'main/add.html', {'hero': heroes, 'h0': h[0], 'h1': h[1], 'h2': h[2], 'h3': h[3]})

headers = {'user-agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
           }


def sort_tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup


names = ['abaddon', 'alchemist', 'ancient-apparition', 'anti-mage', 'arc-warden', 'axe', 'bane', 'batrider',
         'beastmaster', 'bloodseeker', 'bounty-hunter', 'brewmaster', 'bristleback', 'broodmother', 'centaur-warrunner',
         'chaos-knight', 'chen', 'clinkz', 'clockwerk', 'crystal-maiden', 'dark-seer', 'dark-willow', 'dawnbreaker',
         'dazzle', 'death-prophet', 'disruptor', 'doom', 'dragon-knight', 'drow-ranger', 'earth-spirit', 'earthshaker',
         'elder-titan', 'ember-spirit', 'enchantress', 'enigma', 'faceless-void', 'grimstroke', 'gyrocopter',
         'hoodwink', 'huskar', 'invoker', 'io', 'jakiro', 'juggernaut', 'keeper-of-the-light', 'kunkka',
         'legion-commander', 'leshrac', 'lich', 'lifestealer', 'lina', 'lion', 'lone-druid', 'luna', 'lycan', 'magnus',
         'marci', 'mars', 'medusa', 'meepo', 'mirana', 'monkey-king', 'morphling', 'muerta', 'naga-siren',
         "natures-prophet", 'necrophos', 'night-stalker', 'nyx-assassin', 'ogre-magi', 'omniknight', 'oracle',
         'outworld-destroyer', 'pangolier', 'phantom-assassin', 'phantom-lancer', 'phoenix', 'primal-beast', 'puck',
         'pudge', 'pugna', 'queen-of-pain', 'razor', 'riki', 'rubick', 'sand-king', 'shadow-demon', 'shadow-fiend',
         'shadow-shaman', 'silencer', 'skywrath-mage', 'slardar', 'slark', 'snapfire', 'sniper', 'spectre',
         'spirit-breaker', 'storm-spirit', 'sven', 'techies', 'templar-assassin', 'terrorblade', 'tidehunter',
         'timbersaw', 'tinker', 'tiny', 'treant-protector', 'troll-warlord', 'tusk', 'underlord', 'undying', 'ursa',
         'vengeful-spirit', 'venomancer', 'viper', 'visage', 'void-spirit', 'warlock', 'weaver', 'windranger',
         'winter-wyvern', 'witch-doctor', 'wraith-king', 'zeus']
# def counters():  #возвращает контрпики всех персов
#     res = {}
#     headers = {'user-agent':
#                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
#                # нужно найти user-agent свой на сайте и вставить сюда   вот твой:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82
#
#                }
#     for x in names:
#         response = requests.get(f'https://www.dotabuff.com/heroes/{x}/counters', headers=headers)
#         soup = BeautifulSoup(response.text, 'lxml')
#         bv = soup.find_all('tbody')[-1].find_all('tr')
#         lst = []
#         for j in range(len(bv)):
#             s = bv[j]
#             name = s.find('td', class_="cell-xlarge").text
#             d = s.find_all('td')[2].text[:-1]
#             wr = s.find_all('td')[3].text[:-1]
#             lst.append([name, float(d), float(wr)])
#         res[x] = sort_tuple(lst)[:5] + sort_tuple(lst)[-5:]
#     print('ready!')
#     return res
list = ['abaddon', 'alchemist', 'ancient-apparition', 'anti-mage', 'arc-warden', 'axe', 'bane', 'batrider',
        'beastmaster', 'bloodseeker', 'bounty-hunter', 'brewmaster', 'bristleback', 'broodmother', 'centaur-warrunner',
        'chaos-knight', 'chen', 'clinkz', 'clockwerk', 'crystal-maiden', 'dark-seer', 'dark-willow', 'dawnbreaker',
        'dazzle', 'death-prophet', 'disruptor', 'doom', 'dragon-knight', 'drow-ranger', 'earth-spirit', 'earthshaker',
        'elder-titan', 'ember-spirit', 'enchantress', 'enigma', 'faceless-void', 'grimstroke', 'gyrocopter',
        'hoodwink', 'huskar', 'invoker', 'io', 'jakiro', 'juggernaut', 'keeper-of-the-light', 'kunkka',
        'legion-commander', 'leshrac', 'lich', 'lifestealer', 'lina', 'lion', 'lone-druid', 'luna', 'lycan', 'magnus',
        'marci', 'mars', 'medusa', 'meepo', 'mirana', 'monkey-king', 'morphling', 'muerta', 'naga-siren',
        "natures-prophet", 'necrophos', 'night-stalker', 'nyx-assassin', 'ogre-magi', 'omniknight', 'oracle',
        'outworld-destroyer', 'pangolier', 'phantom-assassin', 'phantom-lancer', 'phoenix', 'primal-beast', 'puck',
        'pudge', 'pugna', 'queen-of-pain', 'razor', 'riki', 'ringmaster' ,'rubick', 'sand-king', 'shadow-demon', 'shadow-fiend',
        'shadow-shaman', 'silencer', 'skywrath-mage', 'slardar', 'slark', 'snapfire', 'sniper', 'spectre',
        'spirit-breaker', 'storm-spirit', 'sven', 'techies', 'templar-assassin', 'terrorblade', 'tidehunter',
        'timbersaw', 'tinker', 'tiny', 'treant-protector', 'troll-warlord', 'tusk', 'underlord', 'undying', 'ursa',
        'vengeful-spirit', 'venomancer', 'viper', 'visage', 'void-spirit', 'warlock', 'weaver', 'windranger',
        'winter-wyvern', 'witch-doctor', 'wraith-king', 'zeus']

def counter1(x):
    res = {}
    response = requests.get(f'https://www.dotabuff.com/heroes/{x}/counters', headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    bv = soup.find_all('tbody')[-1].find_all('tr')
    lst = []
    for j in range(len(bv)):
        s = bv[j]
        name = s.find('td', class_="cell-xlarge").text.lower().replace(' ', '-').replace("'", '')
        d = s.find_all('td')[2].text[:-1]
        res[name]= float(d)
    return res

def picker(lst):
    f_data = {}
    for i in list[:]:
        f_data[i] = 0
    for hero_name in lst[1:]:
        data = counter1(hero_name)
        for hero in data.keys():
            f_data[hero] += data[hero]
    d = sorted(f_data.items(), key=lambda x: x[1], reverse=True)
    return d
