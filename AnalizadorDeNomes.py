from itertools import count

nome = str(input('Digite seu nome completo : ')).strip()
print('Analizador de Textos.......')
print('O seu nome completo em Maiuscula é: {}' .format(nome.upper()))
print('O seu nome completo em minisculo é: {} ' .format(nome.lower()))
print('O seu nome completo tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras' .format(nome.find('  ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras' .format(separa[0], len(separa[0])))