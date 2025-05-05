primeiro = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual é razao: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo, razao):
    print('{}' .format(c), end=' -> ')
print('Acabou')
