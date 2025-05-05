num = int(input('Digite um número e vamos achar o seu factorial: '))
c =num
fator = 1
while c > 0:
    fator *= c
    c -= 1
print(f'Fatorial de {num} é igual a {fator}')