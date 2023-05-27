#Exercicio10
'''Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchida pelo usuário,
porém não deve conter valores repitidos.Exibir no final da lista'''
C = 0
L = []
Ultimo = 0
while C < 16:
    N = int(input('Digite um número para adicionar na lista:'))
    if N != Ultimo:
        L.append(N)
    Ultimo = N
    C = C + 1
print('A lista é {}'.format(L))
