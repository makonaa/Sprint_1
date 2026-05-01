world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
# №1 - added Argentina to world_champions
world_champions[2022] = 'Аргентина'

# №2 - displayed world_champions in format: <year> - <champion>
for key, value in world_champions.items():
    print(f'{key} - {value}')

# №3 - defined whether Italy has won Football World Championship in XXI century
world_champions_country_list = list(world_champions.values())
country = 'Италия'

if country in world_champions_country_list:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')


