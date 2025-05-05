from datetime import date
ano = int(input('Informe a sua data de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    tempo = 18 - idade
    print('O jovem está com {} anos e faltam {} anos para se alistar'.format(idade, tempo))
elif idade == 18:
    print('O jovem está com {} anos e precisa se alistar imediatamente!'.format(idade))
else:
    tempo = idade - 18
    print('O jovem está com {} anos e já passou {} anos do tempo de se alistar!'.format(idade, tempo))
