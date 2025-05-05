from random import randint

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1,10))

#def soma():

numeros = list()
sorteia(numeros)
print(numeros)
