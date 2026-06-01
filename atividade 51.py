def_q51():
    contador = 1
    
    preco = float(input("Digite o preço do produto 1: "))
    maior = preco
    menor = preco
    
    contador = 2
    
    while contador <= 8:
        preco = float(input(f"Digite o preço do produto {contador}: "))
    
        if preco > maior:
            maior = preco
    
        if preco < menor:
            menor = preco
    
        contador += 1
    
    print("Maior preço:", maior)
    print("Menor preço:", menor)
    
    input()