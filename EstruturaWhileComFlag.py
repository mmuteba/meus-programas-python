
count = soma = 0
numero = int(input('Digite um número [999 é a flag para parar]: '))
while numero != 999:
    count += 1
    soma += numero
    numero = int(input('Digite um número [999 é a flag para parar]: '))
print(f'Foram digitados {count} numeros e a soma deles da um universo de {soma}')