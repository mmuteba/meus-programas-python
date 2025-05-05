velocidade = int(input('Qual e a velocidade do carro? '))
multa = 1200 * (velocidade - 80)
if velocidade > 80:
    print('VELOCIDADE ACIMA DA MÉDIA {} Km/h, voce foi multado! A sua multa sera de {} kz ' .format(velocidade, multa))
else:
    print('Boa velocidade! Conduza com segurança!')