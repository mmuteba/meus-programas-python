salario = float(input('Qual é o valor do salário? '))

if salario > 200:
    salarioA = salario + (salario * 0.1)
    print('O salário é de {:.2f} kz e terá um acrescimo de 10%, que perfaz um valor total de {:.2f} kz' .format(salario, salarioA))
else:
    salarioA = salario + (salario * 0.15)
    print('O salário atual é de {:.2f} kz e terá um acrescimo de 15%, perfazendo um total de {:.2f} kz' .format(salario, salarioA))
