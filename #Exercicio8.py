#Exercicio8
'''Elaborar um programa que contem uma lista com numero elementos, essa lista deve ser prenchida pelo usuário e só deve
conter números inteiros positivos e pares.Caso o usúario digite o número 1 a repetição termina imediatamente.
exibir no final os elementos da lista'''

lista = []
numero = 0
cont = 0
elementos = int(input('Digite quantos elementos deve ter lista:'))

while cont >= 0 and cont < elementos and numero != 1:

    numero = int(input('Digite um número inteiro e par para adicionar na lista:'))

    if numero % 2 == 0:
      lista.append(numero)
      cont += 1

print('A lista é {}'.format(lista))
      
