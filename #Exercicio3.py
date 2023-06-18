#Exercicio3

'''Elaborar um programa que deve ler num números.
Caso o usúario digite zero (0),o programa deve exibit a somatória e a média dos valores inseridos.'''

num = 1 
soma = 0
cont = 0

print('Digite um número para somar e mostrar a media,Para finalizar Digite 0')

while num != 0:

    if num != 0:
      num = float(input('Digite:'))
      soma = soma + num
      cont = cont + 1

media = soma / cont

print('A Soma é {} \n A media é {}'.format(soma, media))
