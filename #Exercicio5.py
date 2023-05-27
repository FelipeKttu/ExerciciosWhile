#Exercicio5
#Elaborar um programa que lê um número N inteiro maior que 2 (caso N não for maior que 2 deve solicitar outro
# número).Logo após o programa deve exibir o quadrado e o cubo de 2 até N 
N = 0
C = 1
X = 0
while N < 2:
    N = int(input('Digite um número maior que 2:'))
for C in range(2,N):
    N = C 
    Q = N * N
    CB = N * N * N
    C += 1
    print('O seu numero é {} Seu quadrado é {} Seu cubo é {}'.format(N,Q,CB))