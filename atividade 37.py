def_q37():
    salario = float(input("Digite o salário atual: R$ "))
    genero = input("Digite o gênero (M/F): ").strip().upper()
    anos = int(input("Quantos anos trabalha na empresa? "))
    
    # cálculo do aumento
    if genero == "F":
        if anos < 15:
            aumento = 0.05
        elif anos <= 20:
            aumento = 0.12
        else:
            aumento = 0.23
    
    elif genero == "M":
        if anos < 20:
            aumento = 0.03
        elif anos <= 30:
            aumento = 0.13
        else:
            aumento = 0.25
    
    else:
        print("Gênero inválido!")
        aumento = 0
    
    # novo salário
    novo_salario = salario + (salario * aumento)
    
    print(f"Novo salário: R${novo_salario:}")
    
    
    input()
