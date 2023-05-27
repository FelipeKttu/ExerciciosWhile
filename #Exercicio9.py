#Exercicio9
''''Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve prencher com valores
reais. logo em seguida, deve ser solicitado ao usuário que digite dois números. Esses números devem corresponder
a posiçoes na lista (caso contrário solicite um novo valor). Após inserir dois números o programa deve exibir
a soma dos elementos das duas posições da lista'''
C = 0
V = 0
L = []

while C < 5:
    V = float(input('Digite um valor real para adicionar a lista:'))
    L.append(V)
    C = C + 1

P1 = int(input('Digite a primeira posição da lista para somar:'))
P2 = int(input('Digite a segunda posição da lista para somar: '))

if P1 > 0 and P1 < 6 and P2 > 0 and P2 < 6:
   P1Valor = L[P1 - 1]
   P2Valor = L[P2 - 1]
   Soma = P1Valor + P2Valor
   print('A soma da posição {} com valor {} e da segunda posição {} de valor {} é {}'.format(P1,P1Valor,P2,P2Valor,Soma))