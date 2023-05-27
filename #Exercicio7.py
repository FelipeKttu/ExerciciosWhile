#Exercicio7
V = 0
I = 1
while I != 0:
    print('-=-'* 5,'Cardapio UMC Lanches','-=-' * 5)
    print('Para comprar Cachorro Quente digite 100\nPara comprar Bauru simples digite 101')
    print('Para comprar Bauru c/ovo digite 102 \nPara comprar Hamburger digite 103')
    print('Para comprar Chesse Burguer digite 104 \nPara comprar refrigerante digite 105')
    print('-=-'* 5,'Cardapio UMC Lanches','-=-' * 5)
    I = int(input('Digite o codigo do item:'))
    if I == 100:
        V = V + 3.50
    elif I == 101:
        V = V + 3.80
    elif I == 102:
        V = V + 4.50
    elif I == 103:
        V = V + 4.70
    elif I == 104:
        V = V + 5.30
    elif I == 105:
        V = V + 4.00
    elif I < 100 or I > 105 or I == 0:
        print('Número invalido !!')
print('Seu pedido deu {:.2f}'.format(V))
      

