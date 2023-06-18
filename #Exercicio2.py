#Exercicio2
'''Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana correpondente.
O programa deve repetir até que o usuário digite um número fora desse intervalo,caso isso aconteça o algortimo
mostra uma mensagem informando "Número inválido !!'''

num = 1

while num >= 1 and num <= 7:

    num = int(input('Digite o dia da semana(Número):'))

    if num == 1:
        print('Hoje é Domingo !!')
    elif num == 2:
        print('Hoje é Segunda !!')
    elif num == 3:
       print('Hoje é Terça !!')
    elif num == 4:
        print('Hoje é Quarta !!')
    elif num == 5:
        print('Hoje é Quinta !!')
    elif num == 6:
        print('Hoje é Sexta !!')
    elif num == 7:
        print('Hoje é Sabádo')
if num <= 0 or num > 7:
    print('Número Invalido !!')
