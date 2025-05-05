from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CartDeTrabalho'] = int(input('Nº Da Carteira de Trabalho [0 não tem]: '))
if dados['CartDeTrabalho'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: Kz'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-=' *30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')