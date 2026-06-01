def_q35():
    print("=== ALUGUEL DE CARROS ===")
    
    tipo = input("Tipo de carro (popular/luxo): ").lower()
    dias = int(input("Quantos dias de aluguel: "))
    km = float(input("Quantos Km percorridos: "))
    
    if tipo == "popular":
        preco_dia = 90
        
        if km <= 100:
            preco_km = 0.20
        else:
            preco_km = 0.10
    
    elif tipo == "luxo":
        preco_dia = 150
        
        if km <= 200:
            preco_km = 0.30
        else:
            preco_km = 0.25
    
    else:
        print("Tipo de carro inválido!")
        exit()
    
    total = (dias * preco_dia) + (km * preco_km)
    
    print(f"\nTotal a pagar: R$ {total:.2f}")
    
    
    input()
