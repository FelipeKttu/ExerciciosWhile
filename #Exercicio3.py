#Exercicio3
'''Elaborar um programa que deve ler N números.
Caso o usúario digite zero (0),o programa deve exibit a somatória e a média dos valores inseridos.'''
N = 1 
S = 0
Cont = 0
print('Digite um número para somar e mostrar a media,Para finalizar Digite 0')
while N != 0:
    if N != 0:
      N = float(input('Digite:'))
      S = S + N
      Cont = Cont + 1
M = S / Cont

print('A Soma é {} \n A media é {}'.format(S,M))