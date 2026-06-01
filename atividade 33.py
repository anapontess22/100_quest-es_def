def_q33():
    print("=== APROVAÇÃO DE EMPRÉSTIMO ===")
    
    # Entrada de dados
    valor_casa = float(input("Digite o valor da casa: R$ "))
    salario = float(input("Digite o seu salário: R$ "))
    anos = int(input("Em quantos anos vai pagar: "))
    
    meses = anos * 12
    prestacao = valor_casa / meses
    limite = salario * 0.30
    
    print(f"\nPrestação mensal: R$ {prestacao:.2f}")
    print(f"Limite permitido (30% do salário): R$ {limite:.2f}")
    
    if prestacao <= limite:
        print("Empréstimo APROVADO!")
    else:
        print("Empréstimo NEGADO!")
        
        
    input()
        
        