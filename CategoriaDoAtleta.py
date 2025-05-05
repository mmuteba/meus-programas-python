from datetime import date
ano = int(input('Qual e a sua data de nascimento? '))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta tem {} anos faz parte da categoria MIRIM' .format(idade))
elif idade <= 14:
    print('O atleta te {} anos e faz parte da categoria INFANTIL ' .format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e faz parte da categoria JUNIOR ' .format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e faz poarte da categoria SENIOR' .format(idade))
else:
    print('O atleta tem {} anos e faz parte da categoria MASTER' .format(idade))