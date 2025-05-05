aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if 10 <= aluno['média'] <= 20:
    aluno['situacao'] = 'Aprovado!'
elif 7 <= aluno['média'] < 10:
    aluno['situacao'] = 'Recurso!'
elif 0 <= aluno['média'] < 7:
    aluno['situacao'] = 'Reprovado!'
else:
    aluno['situacao'] = 'Média inválida! Coloque um número entre 0 e 20!'
print('=-' *30)
for k, v in aluno.items():
    print(f' - {k} = {v}')