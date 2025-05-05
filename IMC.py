peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
'''INDICE DE MASSA CORPORAL'''
IMC = peso/(altura ** 2)
print('O índice de massa corporal é de {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do peso')
elif  18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')