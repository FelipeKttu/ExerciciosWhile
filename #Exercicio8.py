#Exercicio8
'''Elaborar um programa que contem uma lista com N elementos.essa lista deve ser prenchida pelo usuário e só deve
conter números inteiros positivos e pares.Caso o usúario digite o número 1 a repetição termina imediatamente.
exibir no final os elementos da lista'''
L = []
N = 0
C = 0
E = int(input('Digite quantos elementos deve ter lista:'))
while C >= 0 and C < E and N != 1:
    N = int(input('Digite um número inteiro e par para adicionar na lista:'))
    if N % 2 == 0:
      L.append(N)
      C += 1
print('A lista é {}'.format(L))