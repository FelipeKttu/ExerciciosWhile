"""Exercicio2
Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana correpondente.
O programa deve repetir até que o usuário digite um número fora desse intervalo,caso isso aconteça o algortimo
mostra uma mensagem informando "Número inválido !!"""

N = 1
while N >= 1 and N <= 7:
    N = int(input('Digite o dia da semana(Número):'))
    if N == 1:
        print('Hoje é Domingo !!')
    elif N == 2:
        print('Hoje é Segunda !!')
    elif N == 3:
       print('Hoje é Terça !!')
    elif N == 4:
        print('Hoje é Quarta !!')
    elif N == 5:
        print('Hoje é Quinta !!')
    elif N == 6:
        print('Hoje é Sexta !!')
    elif N == 7:
        print('Hoje é Sabádo')
if N <= 0 or N > 7:
    print('Número Invalido !!')
