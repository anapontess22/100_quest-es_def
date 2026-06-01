def_q23():
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo (M/F): ").upper()
    valor = float(input("Digite o valor da compra: "))
    
    if sexo == "F":
        preco_final = valor - (valor * 0.13)
    else:
        preco_final = valor - (valor * 0.05)
    
    print("Cliente:", nome)
    print("Valor com desconto: R$", round(preco_final, 2))
    input()