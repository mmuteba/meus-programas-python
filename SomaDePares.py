from itertools import count

soma = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o {}º numero: ' .format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print('Voce tem {} numeros pares e a soma deles é {} '.format(count, soma))