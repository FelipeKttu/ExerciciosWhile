#Exercicio10
'''Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchida pelo usuário,
porém não deve conter valores repitidos.Exibir no final da lista'''

cont = 0
lista = []
ultimo = 0

while cont < 16:
    N = int(input('Digite um número para adicionar na lista:'))

    if N != ultimo:
        lista.append(N)

    ultimo = N
    cont = cont + 1
    
print('A lista é {}'.format(lista))
