nome = input('Digite o nome do aluno: ')
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A média de {} e {} fornecidos pelo/a {} é de {} ' .format(n1, n2, nome, m))