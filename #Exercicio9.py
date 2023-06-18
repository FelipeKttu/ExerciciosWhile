#Exercicio9
''''Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve prencher com valores
reais. logo em seguida, deve ser solicitado ao usuário que digite dois números. Esses números devem corresponder
a posiçoes na lista (caso contrário solicite um novo valor). Após inserir dois números o programa deve exibir
a soma dos elementos das duas posições da lista'''

cont = 0
valor = 0
lista = []

while cont < 5:
    valor = float(input('Digite um valor real para adicionar a lista:'))
    lista.append(valor)
    cont = cont + 1

primeira_posic = int(input('Digite a primeira posição da lista para somar:'))
segunda_posic = int(input('Digite a segunda posição da lista para somar: '))

if primeira_posic > 0 and primeira_posic < 6 and segunda_posic > 0 and segunda_posic < 6:
   valorPosic1 = lista[primeira_posic - 1]
   valorPosic2 = lista[segunda_posic - 1]
   soma = valorPosic1 + valorPosic2

   print('A soma da posição {} com valor {} e da segunda posição {} de valor {} é {}'.format(primeira_posic, valorPosic1, segunda_posic, valorPosic2, soma))
