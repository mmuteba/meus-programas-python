p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
media = (p1 + p2 )/2
if media < 7:
    print('O aluno obteve uma média de {} valores, ficando assim  REPROVADO!' .format(media))
elif media < 10:
    print('O aluno vai a RECURSO com {} valores' .format(media))
elif media < 15:
    print('O aluno vai a exame com {}' .format(media))
elif media <= 20:
    print('O aluno dispensa com {} valores' .format(media))
else:
    print('Media invalida! Preste mais atencao!')