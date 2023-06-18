#Exercicio6

"""Elaborar um programa que solicite um número (entre 10 e 15). Se o usuario digitar um número diferente, 
o programa deve mostrar a mensagem "Entrada invalida" e solicitar um número novamente.Se o digitar correto o programa 
deve mostrar a raiz quadrada desse número e o programa termina"""

from math import sqrt

num = int(input('Digite um número entre 10 e 15:'))

while num < 10 or num > 15:
  print('Entrada invalida !!')

  num = int(input('Digite um número entre 10 e 15:'))

raiz = sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, raiz))
