num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        #print('{}'.format(c), end=' ')
        tot += 1
#print('\n"O numero {} foi dividido {} vezes" '.format(num, tot))
if tot == 2:
    print('O número {} é um número PRIMO ' .format(num))
else:
    print('O número {} nao é um número PRIMO ' .format(num))