count = soma = 0
while True:
    numb = int(input('Digite um numero: '))
    if numb == 999:
        break
    count += 1
    soma += numb
print(f'Voce digitou {count} numeros e a soma deles e de: {soma}')