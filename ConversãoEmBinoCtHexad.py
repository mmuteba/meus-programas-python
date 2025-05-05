num = int(input('Digite um número inteiro: '))
print('''EScolha  uma das bases para a conversao:
      [1] para BINÁRIO
      [2] para OCTAL
      [3] para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{}, convertido para Binaio e {}' .format(num, bin(num)[2:]))
elif opcao == 2:
    print('{}, convertido para Octal e {} ' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('{}, convertido para Hexadecimal e {} '. format(num, hex(num)[2:]) )
else:
    print('Opcao inválida! Tente novamente..!')
