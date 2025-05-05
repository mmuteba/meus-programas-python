sexo = str(input('Qual é o sexo: ')).strip().upper()[0]
while sexo not in 'MmFf'.upper():
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip()[0]
print(f'Sexo {sexo} registrado com sucesso')
