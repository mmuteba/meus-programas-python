print('=' *15, end=' ')
print('LOJA DO MÁRIO', end=' ')
print('=' *15)
preço = float(input('Preço das compras: Kz'))
print('''FORMAS DE PAGAMENTO: 
    [1] à vista, dinheiro/cheque
    [2] à vista, cartao
    [3] 2 prestaçoes no cartao
    [3] 3 prestaçoes ou mais no cartao''')
opçao = int(input('Qual é a opçao? '))
if opçao == 1:
    ValorPago =  preço - (preço * 0.1)
    print('Sua compra de {} kz, vai custar {:.2f} kz no final!' .format(preço, ValorPago))
elif opçao == 2:
    ValorPago = preço - (preço * 0.05)
    print('Sua compra de {} kz, vai custar {:.2f} kz no final!' .format(preço, ValorPago))
elif opçao == 3:
    print('Sua compra será feita em até 2 prestaçoes no cartao, no preço normal de {} kz' .format(preço))
elif opçao == 4:
    parcelas = int(input('Em quantas parcelas pretende pagar? '))
    ValorPago = preço + (preço * 0.2)
    ValorParcelado = ValorPago /parcelas
    print('Sua compra será parcelada em {} prestaçoes de {:.2f} kz com JUROS!' .format(parcelas, ValorParcelado))
    print('Sua compra de {} kz, vai custar {:.2f} kz no final'.format(preço, ValorPago))
else:
    print('Opçao Inválida, Tente novamente!')