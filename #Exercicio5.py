#Exercicio5#Exercicio5

'''Elaborar um programa que lê um número num inteiro maior que 2 (caso o número não for maior que 2 deve solicitar outro
número). Logo após o programa deve exibir o quadrado e o cubo de 2 até o número '''

num = 0
cont = 1

while num < 2:

    num = int(input('Digite um número maior que 2:'))

for cont in range(2,num):

    num = cont 
    quadrado = num * num
    cubo = num * num * num
    cont += 1

    print('O seu numero é {} Seu quadrado é {} Seu cubo é {}'.format(num, quadrado, cubo))
