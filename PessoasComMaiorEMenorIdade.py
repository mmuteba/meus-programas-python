from datetime import date
ano = date.today().year
count = 0
cont = 0
for c in range (1, 8, 1):
    idade = int(input('Em que ano a {}º pessoa nasceu? ' .format(c)))
    if (ano - idade) < 18:
        count += 1
    elif (ano -idade) >= 18:
        cont += 1
print('Ao todo tivemos {} pessoas maiores de idade' .format(cont))
print('E também tivemos {} pessoas menores de idade '.format(count))