soma = 0
for n in range(1, 501):
    if n % 2 == 1:
        if n % 3 == 0:
            soma +=  n
print(soma , end=' ')