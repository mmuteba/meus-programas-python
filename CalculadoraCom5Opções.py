num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opçao = 0
while opçao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opçao = int(input('Qual é a sua opçao? '))
    if opçao == 1:
        soma = num1 + num2
        print(f'A soma de {num1} e {num2} é igual a {soma}')
    elif opçao == 2:
        mult = num1 * num2
        print(f'A multiplicaçao de {num1} vezes {num2} é igual a {mult}')
    elif opçao == 3:
        if num1 > num2:
            print(f'O {num1} é maior que {num2}')
        else:
            print(f'O {num2} é maior que o {num1}')
    elif opçao == 4:
        print('Informe os números novamente!')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opçao == 5:
        print('Finalizando o programa....')
    else:
        print('Voce digitou um número inválido! por favor tente novamente...')
    print('=-=' *12)
print('Fim do Programa, volte sempre!')