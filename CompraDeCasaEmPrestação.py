casa = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o salário do comprador? '))
#ano = int(input('Em quantos anos vai pagar? '))
#prestacao = casa / (ano * 12)

minimo = (sal * 0.3)
'''if prestacao <= minimo:
    print('O teu salário é de {:.2f} kz e 30% dele é {:.2f}, o que nos permite aceitar o empréstimo!'.format(sal, minimo))
    print('A casa será paga em {} anos, com uma renda mensal de {:.2f} kz' .format(ano, prestacao))
else:
    print('Empréstimo negado! O valor a pagar excederia 30% do seu salário!')
'''
ano = casa / minimo *12
print('A casa sera paga em {} anos' .format(ano))