"""Exercicio1
Elaborar um programa que solicita varias temperaturas em Graus Celsius, para cada temperatura inserida,
o programa deve converter a para graus Fahrenheit e Kelvin e mostrar na tela
o programa termina quando a temperatura inserida for menor que -5"""
T = 0
while (T > -5):
    T = float(input('Digite uma temperatura em Celsius que queira converter para Fahrenheit e Kelvin:'))
    F = T * 1.8 + 32
    K = T + 273
    print('{}° Celsius são {}° Fahrenheit e {}°Kelvin'.format(T,F,K))
    