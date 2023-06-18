#Exercicio7
'''Faça um cardapio'''

valor = 0
item = 1

while item != 0:

    print('-=-'* 5,'Cardapio Kttu Lanches','-=-' * 5)

    print('Para comprar Cachorro Quente digite 100\nPara comprar Bauru simples digite 101')
    print('Para comprar Bauru c/ovo digite 102 \nPara comprar Hamburger digite 103')
    print('Para comprar Chesse Burguer digite 104 \nPara comprar refrigerante digite 105')
    
    print('-=-'* 5,'Cardapio Kttu Lanches','-=-' * 5)

    item = int(input('Digite o codigo do item:'))
    
    if item == 100:
        valor = valor + 3.50
    elif item == 101:
        valor = valor + 3.80
    elif item == 102:
        valor = valor + 4.50
    elif item == 103:
        valor = valor + 4.70
    elif item == 104:
        valor = valor + 5.30
    elif item == 105:
        valor = valor + 4.00
    elif item < 100 or item > 105 or item == 0:
        print('Número invalido !!')
print('Seu pedido deu {:.2f}'.format(valor))
