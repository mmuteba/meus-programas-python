times = ('Liverpool', 'Barcelona', 'Arsenal', 'Inter de Milão', 'Atlético de Madrid', 'Bayer Leverkusen',
         'Lille', 'Aston Villa','Atalanta', 'Borussia Dortmund', 'Real Madrid', 'Bayern de Munique', 'AC Milan',
         'PSV Eindhoven', 'Paris Saint-Germain', 'Benfica', 'Mónaco', 'Brest', 'Feyenoord', 'Juventus','Celtic',
         'Manchester City', 'Sporting', 'Club Brugge', 'Dínamo de Zagreb','VfB Stuttgart', 'Shakhtar Donetsk',
         'Bologna', 'Estrela Vermelha', 'Sturm Graz', 'Sparta Praga', 'RB Leipzig', 'Girona', 'RB Salzburg',
         'Slovan Bratislava', 'Young Boys')
print('=' *30)
print(f'Lista de times da Champions:')
c = 0
for t in times:
    c += 1
    print(f'{c}º', t)
print('=' *100)
print(f'Os 8 primeiros colocados sao: {times[0:8]}')
print('=' *100)
print(f'Os últimos 5 colocados sao: {times[-5:]}')
print('=' *100)
#print(f'Os times em ordem alfabetica seria {sorted(times)}')
print('=' *100)
print(f'O Real Madrid está na {times.index('Real Madrid') +1 }ºposicao ')