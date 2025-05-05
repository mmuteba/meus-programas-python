print('Gerador de PA')
print('-=' *10)
primeiroT = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
termos = primeiroT
count = 1
while count <= 10:
    print(f'{termos} -> ', end='')
    count += 1
    termos += razao
print('FIM')