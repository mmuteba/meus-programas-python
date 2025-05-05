H = int(input('Qual é a altura da parede: '))
L = int(input('Qual é a largura da parede: '))
A = H * L
T = A/2
print('O cálculo da altura de {}m vezes a largura de {}m da parede, da uma área de {}m2, \n o que implica que precisamos de {} litros de tinta, considerando que para 1 litro de tinta cobrimos 2m2 da parede' .format(H, L, A, T))