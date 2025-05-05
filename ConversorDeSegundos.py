def convert9(segundos):
    horas = segundos // 3600
    seg_rest = segundos % 3600
    min = seg_rest / 60
    seg_finais = seg_rest % 60

    return horas, min, seg_finais

entrada = int(input('Digite os segundos: '))
h, m, s = convert9(entrada)

print(f'{entrada}s equivalem a {h}h: {m}min : {s}seg')