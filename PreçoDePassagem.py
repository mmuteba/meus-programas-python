distancia = int(input('Qual é a distacia a ser percorrida?'))
if distancia <= 200:
    passagem = distancia * 80
    print('Voce está prestes a começar uma viagem de {} Km' .format(distancia))
    print('O preço da passagem será de {} kz' .format(passagem))
else:
    passagem = distancia *70
    print('Voce está prestes a começar uma viagem de {} Km'.format(distancia))
    print('O preço da passagem será de {} kz'.format(passagem))