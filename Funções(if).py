nome = input("Digite seu nome: ")
pedido= int(input("Clique"))
pedido1= input ("Qual seria o lanche escolhido? \n (1-Bigmac/ 2- Cheddar McMelt/ 3- McChicken )")

if pedido >= 1:
    if pedido1 == "1":
        print("Seu Bigmac estará pronto daqui alguns minutos")
    elif pedido1 == "3":
        print("Seu McChicken estará pronto daqui alguns minutos")
    else:
        print ("Seu Cheddar McMelt estará pronto daqui alguns minutos")
