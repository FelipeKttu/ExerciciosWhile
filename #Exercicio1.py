#Exercicio1
'''Elaborar um programa que solicita varias temperaturas em Graus Celsius, para cada temperatura inserida,
o programa deve converter a para graus Fahrenheit e Kelvin e mostrar na tela
o programa termina quando a temperatura inserida for menor que -5 '''

temperatura = 0

while (temperatura > -5):

    temperatura = float(input('Digite uma temperatura em Celsius que queira converter para Fahrenheit e Kelvin:'))
    fahrenheit = temperatura * 1.8 + 32
    kelvin = temperatura + 
    
    print('{}° Celsius são {}° Fahrenheit e {}°Kelvin'.format(temperatura, fahrenheit, kelvin))
    
