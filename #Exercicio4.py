#Exercicio4
'''Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar
o número 100 o programa deve termina, mostrando quantos valores foram acima de 80, quantos foram abaixo de 10 e mostrar
a media de todos os valores digitados pelo usuário '''

N = 0
C = 0
Maior80 = 0
Menor10 = 0
S = 0

while N != 100:
  
  N = float(input('Digite um valor:'))

  if N > 0 and N != 100:

    C = C + 1
    S = S + N
    M = S / C

    if N > 80:
        Maior80 += 1

    elif N < 10:
        Menor10 += 1
        
print('{} São maiores que 80\n{} São menores que 10 \nA media é {}'.format(Maior80,Menor10,M))

