from datetime import date

def voto(ano_nasc):
    idade = date.today().year  - ano_nasc
    if  18 <= idade < 60:
        return f'Com {idade} anos: Voto Obrigatório'
    elif idade >= 60:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Negado'

ano = int(input('Em que ano voce nasceu? '))
print(f'{voto(ano)}')
