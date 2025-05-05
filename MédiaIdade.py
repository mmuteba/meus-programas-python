soma = 0
mIdade = 0
for p in range(1, 5):
    print(f'------- {p}º pessoa -----------')
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    soma += idade
    sexo = str(input('Digite o sexo: [M/F]')).strip()
mIdade = soma/4
print(f'A média de idade é: {mIdade}')